from django.urls import path

from . import views

app_name='pages_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('events-demo-1/', views.events_demo_1, name='events_demo_1'),
    path('events-demo-2/', views.events_demo_2, name='events_demo_2'),
]
