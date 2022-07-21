from django.urls import path
from . import views


app_name = 'java_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todo, name='todo'),
    path('phrase', views.phrase, name='phrase'),
    path('passwordgent/', views.passwordgent, name='passwordgent'),
    path('unitconverter/', views.unitconverter, name='unitconverter'),

]
