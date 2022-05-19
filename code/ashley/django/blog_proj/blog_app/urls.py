from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile')
    path('create/', views.create, name='create')
]