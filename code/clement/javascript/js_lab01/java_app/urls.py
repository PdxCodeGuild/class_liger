from django.urls import path
from . import views


app_name = 'java_app'

urlpatterns = [
    path('', views.phrase, name='phrase'),
    path('todolist/', views.todolist, name='todolist'),
    path('passwordgent/', views.passwordgent, name='passwordgent'),
    path('unitconverter/', views.unitconverter, name='unitconverter'),

]
