from django.contrib import admin

from .models import Category, Product, Cart

admin.site.register([Category, Product, Cart])