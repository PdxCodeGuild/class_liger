from django.shortcuts import get_object_or_404, render, redirect

from django.urls.base import reverse
from blog_app.forms import BlogForm

from user_app.models import CustomUser

from django.contrib.auth.decorators import login_required

from django.contrib.auth import (
    get_user_model,
)

# Create your views here.


@login_required
def create(request, username):

    if request.method == 'GET':

        print('GET PAGE-2')

        form = BlogForm

        return render(request, 'blog_app/create.html' )

    elif request.method == 'POST':

        print('GET POST-2')

        form = BlogForm

        print(form)

        title = form.get('title')

        body = form.get('body')

        user = get_object_or_404(get_user_model(), username=username)

        

        context = {

            'title': title,
            'body': body,
            'username': username

        }

        return redirect(reverse('user_app:profile', context, kwargs={ 'username': username}))

# ---------------------------------------------------------

def base(request):
    
    return render(request, 'blog_app/base.html')