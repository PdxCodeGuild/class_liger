from django.db import models
from django.contrib.auth import get_user_model
import random

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    # define the plural name for the Category model in the admin panel
    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)
    rating_count = models.PositiveIntegerField(default=0)

    # each product can have many categories,
    # those categories will contain each product
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.title

class Cart(models.Model):
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='cart')

    # through='CartItem' will leverage the 'cart' and 'product' ForeignKey fields
    # in the CartItem model to allow quantities of each item in a cart to be tracked
    products = models.ManyToManyField(Product, through='CartItem', related_name='carts', null=True, blank=True)


    def item_count(self):
        '''return the sum of the quantities of the cart_items in the cart'''
        count = 0

        for cart_item in self.cart_items.all():
            count += cart_item.quantity

        return count


    def total_price(self):
        '''return the sum of all the prices for all the products in the cart'''
        total = 0

        for cart_item in self.cart_items.all():
            total += cart_item.item_subtotal()

        return total

    def __str__(self):
        return f"{self.owner}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')

    quantity = models.PositiveIntegerField(default=0)

    def item_subtotal(self):
        '''return the subtotal price of a cart item'''
        return self.quantity * self.product.price