from django.urls import path
from . import views

app_name = 'n_plus_one'

urlpatterns = [
    path('', views.index, name='index')
]