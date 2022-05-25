from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_post/', views.write_post, name='write_post'),
    # path('profile/', views.profile, name='profile')
]
