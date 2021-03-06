from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from blog_app.models import BlogPost
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    login as django_login,
    logout as django_logout,
    authenticate,
    get_user_model 
)




def base_view(request):

    context = {

        'blogposts': BlogPost.objects.all().order_by('-date_created')
    }

    return render(request, 'user_app/base.html', context)

# --------------------------------------------------------
    
def register(request):

    if request.method == 'GET':
    
        return render(request, 'user_app/register.html')
    
    elif request.method == 'POST':

        form = request.POST

        username = form.get('username')

        password = form.get('password')

        firstname = form.get('firstname')

        lastname = form.get('lastname')

        email = form.get('email')

        user = CustomUser.objects.create_user(

            firstname=firstname,
            lastname=lastname,
            email=email,
            username=username,
            password=password,
            
        )

        django_login(request, user)

        return redirect(reverse('user_app:profile', kwargs={ 'username': user.username}))    

# --------------------------------------------------------

def login(request):

    if request.method == 'GET':

        return render(request, 'user_app/login.html')

    elif request.method == 'POST':

        form = request.POST

        username = form.get('username')

        password = form.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            django_login(request, user) 

        return redirect(reverse('user_app:profile', kwargs={ 'username': user.username}))




# --------------------------------------------------------
@login_required
def profile(request, username):

    if request.method == 'GET':

        user = get_object_or_404(get_user_model(), username=username)

        context = {

            'username': user,
            
        }

        return render(request, 'user_app/profile.html', context)



# --------------------------------------------------------

def logout(request):
    django_logout(request)

    return redirect('user_app:base_view')