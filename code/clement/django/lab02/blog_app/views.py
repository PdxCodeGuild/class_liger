from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Usersystem, BlogPost

# Create your views here.


@login_required
def profile(request):
    blogpost = BlogPost.objects.all()

    blog_posts = BlogPost.objects.filter(user__icontains=blogpost)

    context = {
        'blogpost': blogpost,
    }

    return render(request, 'users/profile.html', context)


def create(request):
    if request.method == 'POST':
        form = request.POST
        blogpost_title = form.get('blogpost_title')
        blogpost_body = form.get('blogpost_body')
        print(request.user)

        new_blogpost = BlogPost.objects.create(
            user=request.user,
            title=blogpost_title,
            body=blogpost_body

        )
        context = {
            'blogpost': new_blogpost,
        }
        return redirect(request, 'createBlog-post.html', context)

    else:
        return render(request, 'createBlog-post.html')
