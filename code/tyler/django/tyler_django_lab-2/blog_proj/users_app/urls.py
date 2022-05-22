from django.urls import path
from . import views
app_name = 'users_app'

urlpatterns = [
    path('register/', views.register, name='users/register'),
    path('login/', views.login, name='users/login'),
    path('profile', views.profile, name='users/profile')

]
