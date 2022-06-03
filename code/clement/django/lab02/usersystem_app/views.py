from django.shortcuts import render, redirect

from django.contrib.auth import (
    authenticate,
    login as blog_login,
    logout as blog_logout,
    get_user_model,
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Usersystem
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'users/index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')

    elif request.method == 'POST':
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        print(form)

# use the form data to create a new user object (use the create_user method instead of the create method)
        new_usersystem = Usersystem.objects.create_user(
            username=username,
            password=password,
        )

        # login the new user (using django's login function)
        messages.success(request, f'Welcome, {new_usersystem.username}')

        blog_login(request, new_usersystem)
        return redirect('usersystem_app:index')


def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')

    elif request.method == 'POST':
        form = request.POST
        username = form.get('username')
        password = form.get('password')

        usersystem = authenticate(
            request,
            username=username,
            password=password,
        )
    # If the authentication is not correct, render error.
        if usersystem is None:
            messages.error(request, 'Invalid Username or Password')

            return render(request, 'users/login.html')

    # When the user successfully in
        blog_login(request, usersystem)
        print(request.user)
        messages.success(request, f'Welcome Back {usersystem.username}.')
        return redirect('usersystem_app:profile')


def logout(request):
    blog_logout(request)
    return redirect('usersystem_app:login')


@login_required
def profile(request):

    return render(request, 'users/profile.html')
