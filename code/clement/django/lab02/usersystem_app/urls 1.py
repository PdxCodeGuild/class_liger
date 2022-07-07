from django.urls import path
from . import views



app_name = 'usersystem_app'


urlpatterns = [
    path('', views.profile, name = 'profile'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name='login'),
   
]