from django.urls import path

from . import views

app_name='users_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('users/', views.list_users, name='list'),
    path('users/<str:username>', views.detail, name="detail"),
    path('users/edit/<str:username>', views.update, name="update"),
    path('users/follow/<str:username>', views.follow, name="follow")
]