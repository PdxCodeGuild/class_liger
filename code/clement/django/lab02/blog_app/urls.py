from django.urls import path

from . import views


app_name = 'blog_app'




urlpatterns = [
    # path('profile/', views.profile, name = 'profile'),
   
    path('create/', views.create, name='create'),
]