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

        print('GET PAGE-2')

        form = request.GET

        return render(request, 'blog_app/create.html' )

    elif request.method == 'POST':
        
        print('GET POST-2')

        form = request.POST

        print(form)

        title = form.get('title')

        body = form.get('body')        

        user = get_object_or_404(get_user_model(), username=request.user)

        # print(request.user.posts.all())        

        blogpost = BlogPost.objects.create(

            title=title,
            body=body,
            user=user,

        )
        print(blogpost.date_created, blogpost)

        blogposts = BlogPost.objects.all()

        print(blogposts)
        

        # context = {

        #     'blogposts':user.posts.all
        # }

        return redirect(reverse('user_app:profile', args=[request.user.username, ]))

# ---------------------------------------------------------

def base(request):
    
    return render(request, 'blog_app/base.html')