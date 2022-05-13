from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Product, CartItem
from django.db.models import Q

def index(request):

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
        'products': products,
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