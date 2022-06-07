from django.urls import path
from . import views


app_name = 'java_redo_app'

urlpatterns = [

    path('', views.base, name='base'),
    path('uc/', views.uc, name='uc'),
    path('pw/', views.pw, name='pw'),
    path('cc/', views.cc, name='cc'),   

] 