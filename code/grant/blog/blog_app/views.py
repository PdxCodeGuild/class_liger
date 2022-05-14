from django.shortcuts import get_object_or_404, render, redirect

from django.urls.base import reverse
from .models import BlogPost
from user_app.models import CustomUser

from django.contrib.auth.decorators import login_required

from django.contrib.auth import (
    get_user_model,
)

# Create your views here.


@login_required
def create(request):

    if request.method == 'GET':

        form = request.GET

        return render(request, 'blog_app/create.html' )

    elif request.method == 'POST':

        form = request.POST

        title = form.get('title')

        body = form.get('body')        

        user = get_object_or_404(get_user_model(), username=request.user)      

        blogpost = BlogPost.objects.create(

            title=title,
            body=body,
            user=user,

        )
        print(blogpost.date_created, blogpost)

        return redirect(reverse('user_app:profile', args=[request.user.username, ]))

# ---------------------------------------------------------

def base(request):
    
    return render(request, 'user_app/base.html')