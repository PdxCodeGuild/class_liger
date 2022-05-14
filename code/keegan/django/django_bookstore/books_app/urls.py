from django.urls import path

from . import views

app_name='books_app'


urlpatterns = [
    path('', views.index, name="index"),
    path('add-book/', views.add_book, name='add_book')
]