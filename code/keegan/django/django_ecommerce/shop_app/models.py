from django.db import models
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