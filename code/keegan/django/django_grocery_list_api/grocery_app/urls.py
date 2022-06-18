from django.urls import path

from . import views

app_name = 'grocery_app'

urlpatterns = [
    path('', views.grocery_list, name='grocery_list'),
    path('add-item/', views.add_item, name='add_item'),
    path('toggle-cart-status/<int:grocery_item_id>', views.toggle_cart_status, name='toggle_cart_status'), # toggle the in_cart boolean for an item
    path('increment-quantity/<int:grocery_item_id>', views.increment_quantity, name='increment_quantity'), # update the quantity for an item
    path('decrement-quantity/<int:grocery_item_id>', views.decrement_quantity, name='decrement_quantity'), # update the quantity for an item
    path('delete-item/<int:grocery_item_id>', views.delete_item, name='delete_item'), # remove an item from the list
]

