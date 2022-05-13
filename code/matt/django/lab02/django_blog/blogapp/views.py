from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

from .models import User


def index(request):
    return render(request, "authuser/register.html")


def register(request):
    if request.method == "GET":
        return render(request, "authuser/register.html")
    elif request.method == "POST":
        form = request.POST

        username = form.get("username")
        password = form.get("password")

        new_user = User.objects.create_user(username=username, password=password)
        dj_login(request, new_user)

        messages.success(
            request, f"Hi {new_user.username}. Thanks for joining the blog!"
        )

    return render(request, "authuser/profile.html", {"new_user": new_user})


def login(request):
    if request.method == "GET":
        return render(request, "authuser/login.html")
    elif request.method == "POST":
        form = request.POST

        username = form.get("username")
        password = form.get("password")

        user = authenticate(request, username=username, password=password)
        # login(request, user)

        print("********* authenticated user:", user)
        if user is None:
            messages.error(request, "invalid login")
            return render(request, "authuser/login.html")

        dj_login(request, user)

        # messages.success(request, f"Hi {user.username}. Welcome to the blog!")
        # return render(request, "authuser/login.html")
        return redirect("blogapp:profile")


@login_required
def profile(request):
    return render(request, "authuser/profile.html", {"user": request.user})


def logout(request):
    dj_logout(request)
    return redirect("blogapp:login")
