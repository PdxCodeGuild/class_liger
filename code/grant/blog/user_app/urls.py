
from django.urls import path
from . import views


app_name = 'user_app'

urlpatterns = [
    path('', views.base_view, name='base_view'),
    path('login/', views.login, name ='login'),
    path('profile/<str:username>', views.profile, name = 'profile'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout, name = 'logout')
] 