from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('grocery-list/', views.grocery_list, name='grocery_list')
]
