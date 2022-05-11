from django.shortcuts import render
from .models import Category, Product

def index(request):

    products = Product.objects.all()

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

    context = {
        'search_options': search_options,
        'products': products
    }

    return render(request, 'shop/index.html', context)