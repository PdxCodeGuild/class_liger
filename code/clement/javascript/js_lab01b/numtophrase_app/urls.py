from django.urls import path
from . import views


app_name = 'numtophrase_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('phrase/', views.phrase, name='phrase'),

]
