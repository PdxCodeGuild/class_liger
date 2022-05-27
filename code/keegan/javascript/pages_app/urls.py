from django.urls import path

from . import views

app_name='pages_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('events-demo-1/', views.events_demo_1, name='events_demo_1'),
    path('events-demo-2/', views.events_demo_2, name='events_demo_2'),
    path('async-demo-1/', views.async_demo_1, name='async_demo_1'),
    path('async-demo-2/', views.async_demo_2, name='async_demo_2'),
    path('vue-intro/', views.vue_intro, name='vue_intro'),
]
