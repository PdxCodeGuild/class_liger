from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Category, Product, CartItem
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse

def index(request):

    # define defaults for the page number and per_page value
    default_per_page = 5
    default_page_number = 1

    # request.GET holds URL parameters provided in the url of a GET request
    page_number = request.GET.get('page_number') or default_page_number
    per_page = request.GET.get('per_page') or default_per_page


    products = Product.objects.all()

    # if the search form was submitted,
    # apply various filters based on the form data

    # pull the values out of the form
    search_query = request.POST.get('search-query') or ''
    # .getlist will find all fields containing the same name
    categories = request.POST.getlist('categories') or [category.title for category in Category.objects.all()]
    min_price = request.POST.get('min-price') or ''
    max_price = request.POST.get('max-price') or ''
    min_rating = request.POST.get('min-rating') or ''
    max_rating = request.POST.get('max-rating') or ''
    order_by = request.POST.get('order-by') or 'price'

    if search_query:
        # use Q objects to search within the title OR description fields for the search_query
        products = products.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )


    # filter by checked categories using field lookups
    products = products.filter(categories__title__in=categories)


    # apply price filters
    if min_price and not max_price:
        # find products whose price is greater than the min
        products = products.filter(price__gte=min_price)
    elif max_price and not min_price:
        # find products whose price is less than the max
        products = products.filter(price__lte=max_price)
    elif min_price and max_price:
        # find products whose price are between the min and max
        products = products.filter(price__gte=min_price, price__lte=max_price)
        
    # apply rating filters
    if min_rating and not max_rating:
        # find products whose rating is greater than the min
        products = products.filter(rating__gte=min_rating)
    elif max_rating and not min_rating:
        # find products whose rating is less than the max
        products = products.filter(rating__lte=max_rating)
    elif min_rating and max_rating:
        # find products whose rating are between the min and max
        products = products.filter(rating__gte=min_rating, rating__lte=max_rating)
        

    # order the remaining queryset
    products = products.order_by(order_by)


    # create a page object with the remaining products
    products_page = Paginator(products, per_page).get_page(page_number)


    # data for rendering the 'categories' checkboxes
    # and 'order by' select menu
    search_options = {
        'categories': [category.title for category in Category.objects.all()],
        'order_by_options': [
            {'label': 'Price (Low-to-High)', 'value': 'price'},
            {'label': 'Price (High-to-Low)', 'value': '-price'},
            {'label': 'Name (A-Z)', 'value': 'title'},
            {'label': 'Name (Z-A)', 'value': '-title'},
            {'label': 'Rating (Low-to-High)', 'value': 'rating'},
            {'label': 'Rating (High-to-Low)', 'value': '-rating'},
        ]
    }

    form_data = {
        "search_query": search_query,
        "categories": categories,
        "min_price": min_price,
        "max_price": max_price,
        "min_rating": min_rating,
        "max_rating": max_rating,
        "order_by": order_by,
    }


    context = {
        'search_options': search_options,
        'products_page': products_page,
        'form_data': form_data

    }

    return render(request, 'shop/index.html', context)


def add_to_cart(request, product_id):
    '''add the product with the given id to the request.user's cart'''

    product = get_object_or_404(Product, id=product_id)

    # get the CartItem if it exists, otherwise create it
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=request.user.cart)

    # increase the quantity of the cart_item in the cart
    cart_item.quantity += 1

    cart_item.save()

    return redirect('shop_app:index')



def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)

    cart_item.delete()

    return redirect(
        reverse(
            "users_app:detail",
            kwargs={'username': request.user.username}
        )
    )


def update_cart_item(request, cart_item_id):

    cart_item = get_object_or_404(CartItem, id=cart_item_id)

    # get the new quantity from the form
    updated_quantity = request.POST.get("quantity")

    # update the quantity
    cart_item.quantity = int(updated_quantity)

    # commit the changes to the database
    cart_item.save()

    return JsonResponse({
        'itemSubtotal': cart_item.item_subtotal(),
        'cartTotal': request.user.cart.total_price(),
        'cartItemCount': request.user.cart.item_count()
    })


    # if using Django's request/response cycle:
    # return redirect(
    #     reverse(
    #         "users_app:detail",
    #         kwargs={'username': request.user.username}
    #     )
    # )