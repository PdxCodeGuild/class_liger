from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import (
    authenticate, login as django_login, logout as django_logout)
from django.contrib import messages

from blog_app.models import BlogPost
from .models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    elif request.method == 'POST':
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        new_user = CustomUser.objects.create_user(
            username=username,
            password=password
        )

        return render(request, 'users/profile.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    elif request.method == 'POST':
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            django_login(request, user)
            messages.success(request, 'Welcome!')
            return redirect(reverse('users_app:profile'))
        else:
            messages.error(
                request, 'Incorrect username and/or password. Please try again.')
            return render(request, 'users/login.html')


@login_required
def profile(request):
    post = BlogPost.objects.filter(user=request.user)
    context = {
        'posts': post
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    django_logout(request)
    return render(request, 'users/login.html')
