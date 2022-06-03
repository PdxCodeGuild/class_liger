from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('grocery-list/', views.index, name='index'), # view that renders the template with the Vue app
    path('grocery-items/', views.grocery_retrieve, name='retreive'),
    path('grocery-items/<int:grocery_item_id>', views.grocery_retrieve, name='retreive'),
    path('grocery-items/create/', views.grocery_create, name='create'),
    path('grocery-items/update/<int:grocery_item_id>', views.grocery_update, name='update'),
    path('grocery-items/delete/<int:grocery_item_id>', views.grocery_delete, name='delete')
]
