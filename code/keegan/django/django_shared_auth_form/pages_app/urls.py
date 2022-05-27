from django.urls import path

from . import views

app_name='pages_app'

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
]