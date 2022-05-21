from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse

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

        # messages.success(
        #     request, f"Hi {new_user.username}. Thanks for joining the blog!"
        # )

        return render(request, "authuser/new_profile.html", {"new_user": new_user})


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
        return redirect("userapp:profile")


@login_required
def profile(request):
    blogposts = request.user.blogposts.all().order_by("-date_created")
    print(blogposts)
    context = {
        "blogposts": blogposts,
    }

    print(context)
    return render(request, "authuser/profile.html", context)


def new_profile(request):
    return render(request, "authuser/new_profile.html")


# def myposts(request):
#     my_posts = BlogPosts.objects.filter(date_created__lte=timezone.now()).order_by(
#         "-date_created"
#     )

#     context = {
#         "my_posts": my_posts,
#     }
#     return render(request, "authuser/profile.html", context)


# def create(request):
#     if request.method == "GET":
#         return render(request, "authuser/create.html")

#     # else:
#     #     pass
#     elif request.method == "POST":

#         form = request.POST

#         blog_title = form.get("title")
#         blog_body = form.get("body")

#         BlogPosts.objects.create(user=request.user, title=blog_title, body=blog_body)

#     return redirect("blogapp:profile")


def logout(request):
    dj_logout(request)
    return redirect("userapp:login")


# def blogdetails(request):
#     # b_info = BlogPosts.objects.all()
#     user_blog_info = BlogPosts.objects.get(pk=1)
#     print("Myoutput", user_blog_info)
#     return render(request, "authuser/blogdetails.html", {"b_info": user_blog_info})
