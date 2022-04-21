from django.urls import path

from . import views

app_name='polls_app'

urlpatterns = [
    path('', views.index, name="index"),
]