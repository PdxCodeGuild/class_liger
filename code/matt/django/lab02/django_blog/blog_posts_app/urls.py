from django.urls import path
from . import views

app_name = "blog_posts_app"
urlpatterns = [
    path("create/", views.create, name="create"),
    path("delete/<int:blogpost_id>", views.delete, name="delete"),
]
