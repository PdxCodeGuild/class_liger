

from django.urls import path

#importing from the django_todo_app
from . import views


app_name = 'django_todo_app'

urlpatterns = [
    #load the index page when url local host:8000 is entered
    path('', views.index, name='index'),
    path('add/', views.save_todo_item, name='save_todo_item')

]