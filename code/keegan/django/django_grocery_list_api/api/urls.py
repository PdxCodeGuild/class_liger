from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('grocery-items/', views.grocery_retrieve, name='retreive'),
    path('grocery-items/<int:grocery_item_id>', views.grocery_retrieve, name='retreive'),
    path('grocery-items/create/', views.grocery_create, name='create')
]
