from django.urls import path

from . import views

app_name='shop_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart')
]