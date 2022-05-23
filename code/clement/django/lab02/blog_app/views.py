from django.shortcuts import render

from .models import Usersystem

# Create your views here.

def create(request):
    form = request.POST
    # post_text = form.get('blogpost-text')

    new_blogpost = Usersystem.objects.create(
        user= request.user
       
    )
    context = {
        'blogpost': new_blogpost,
    }
    return render (request, 'users/createBlog_post.html', context)

def create(request):
    form = request.POST
    # post_text = form.get('blogpost-text')

    new_blogpost = Usersystem.objects.create(
        user= request.user
       
    )
    context = {
        'blogpost': new_blogpost,
    }
    return render (request, 'users/createBlog_post.html', context)
