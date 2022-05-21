from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# from django.http import HttpResponse

from .models import BlogPosts


# def myview(request):
#     return HttpResponse("hello world!")


@login_required
def create(request):
    if request.method == "GET":
        return render(request, "posts/create.html")

    # else:
    #     pass
    elif request.method == "POST":

        form = request.POST

        blog_title = form.get("title")
        blog_body = form.get("body")

        BlogPosts.objects.create(user=request.user, title=blog_title, body=blog_body)

    return redirect("userapp:profile")


def delete(request, blogpost_id):
    delete_post = get_object_or_404(BlogPosts, id=blogpost_id)

    delete_post.delete()

    return redirect("userapp:profile")
