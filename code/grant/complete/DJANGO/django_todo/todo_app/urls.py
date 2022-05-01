





from django.urls import path
from . import views


app_name = 'todo_app'

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('todos/', views.list_todos, name='list_todos'),
    path('add/', views.add_todo, name='add_todo')
]