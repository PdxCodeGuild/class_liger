from django.urls import path

from . import views

app_name='pics_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('edit/<int:pic_id>', views.update, name="update"),
    path('delete/<int:pic_id>', views.delete, name="delete"),
    path('like/<int:pic_id>', views.like, name='like')
]