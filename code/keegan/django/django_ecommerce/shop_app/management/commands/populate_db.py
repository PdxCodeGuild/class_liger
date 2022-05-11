import requests
from django.core.management.base import BaseCommand
from shop_app.models import Category, Product

import json

class Command(BaseCommand):

    def handle(self, *args, **options):

        # delete all existing Products and Categories
        Product.objects.all().delete()
        Category.objects.all().delete()


        url = "https://fakestoreapi.com/products"

        response = requests.get(url)

        products = response.json()

        # loop through the product list of dictionaries
        for product in products:
            # get the data for the current product
            title = product.get('title')
            price = float(product.get('price'))
            description = product.get('description')
            category_title = product.get('category')
            rating = float(product.get('rating').get('rate'))
            rating_count = int(product.get('rating').get('count'))
            image_url = product.get('image')

            # create Product/Category objects with the data from each
            product = Product.objects.create(
                title=title,
                price=price,
                description=description,
                rating=rating,
                rating_count=rating_count,
                image_url=image_url
            )

            # use get_or_create to either fetch the category from the db
            # if it exists or create it if it doesn't
            category, created = Category.objects.get_or_create(title=category_title)
        
            # add the category to the product's list of categories
            product.categories.add(category)
