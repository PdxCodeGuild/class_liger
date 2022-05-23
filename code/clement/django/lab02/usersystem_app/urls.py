from django.urls import path
from . import views

app_name = 'usersystem_app'

urlpatterns = [
    path('', views.register, name = 'register'),
    # path('profile/<str:username>', views.profile, name = 'profile'),
    path('profile/', views.profile, name = 'profile'),
    path('login/', views.login, name='login'),
    path('create/', views.create, name='create'),
]