from django.urls import path

from . import views

app_name = "userapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("new_profile/", views.new_profile, name="new_profile"),
    path("login/", views.login, name="login"),
    # path("create/", views.create, name="create"),
    path("logout/", views.logout, name="logout"),
    # path("blogdetails/", views.blogdetails, name="blogdetails"),
]
