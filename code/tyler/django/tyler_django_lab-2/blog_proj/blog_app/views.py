from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import (
    authenticate, login as django_login, logout as django_logout)
from django.contrib import messages
from .models import CustomUser, BlogPost
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')


@login_required
def create_post(request):
    if request.method == 'GET':
        return render(request, 'blog/create_post.html')
    elif request.method == 'POST':

        form = request.POST
        title = form.get('blog_title')
        body = form.get('blog_body')
        user = request.user
        post = BlogPost.objects.create(user=user,
                                       title=title, body=body)

        return redirect(reverse('users_app:profile'))


@login_required
def write_post(request):
    if request.method == 'link':
        return render(request, 'blog_app:create_post')


def profile_link(request):
    if request.method == 'link':
        return redirect(reverse('users/profile.html'))
