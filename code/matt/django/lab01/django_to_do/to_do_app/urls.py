from django.urls import path

from . import views

app_name = "to_do_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("delete/<int:to_do_item_id>", views.delete, name="delete"),
]
