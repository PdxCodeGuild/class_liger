





from django.urls import path
from . import views


app_name = 'todo_app'

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('add', views.save_todo_items, name='save_todo_items'),
    path('list', views.list_todos, name='list_todos')
]