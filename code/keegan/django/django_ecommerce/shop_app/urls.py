from django.urls import path

from . import views

app_name='shop_app'

urlpatterns = [
    path('', views.index, name='index')
]