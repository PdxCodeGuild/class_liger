from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('save_item/', views.save_todo_item, name = "save_todo_item")
]