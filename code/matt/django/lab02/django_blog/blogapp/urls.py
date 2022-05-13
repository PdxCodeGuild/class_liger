from django.urls import path

from . import views

app_name = "blogapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
