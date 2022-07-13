from django.urls import path

from . import views

app_name = 'pages_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('JS_Lab_1.html/', views.JS_Lab_1, name='Lab_1'),
    path('JS_Lab_2.html/', views.JS_Lab_2, name='Lab_2'),
    path('JS_lab_3.html', views.JS_Lab_3, name='Lab_3')
]
