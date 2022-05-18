from django.urls import path

from . import views

app_name='shop_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_item_id>', views.remove_from_cart, name="remove_from_cart"),
    path('update-cart-item/<int:cart_item_id>', views.update_cart_item, name='update_cart_item')
]