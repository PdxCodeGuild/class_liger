from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import UserForm, UserAuthForm
from django.contrib.auth import (
    login as django_login,
    logout as django_logout,
    authenticate,
    get_user_model # return the value of AUTH_USER_MODEL from settings.py
)
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from shop_app.models import Product

def index(request):
    return render(request, 'pics/index.html')


def register(request):

    if request.method == 'GET':
        # instantiate a blank User form
        form = UserAuthForm()


    elif request.method == 'POST':
        # instantiate the UserAuthForm and populate the 
        # fields with the data from the HTML form
        form = UserAuthForm(request.POST)

        if form.is_valid():
            # create new user object, 
            # but don't save it to the database yet (commit=False)
            new_user = form.save(commit=False)

            # hash the user's password
            # using the validated form data
            new_user.set_password(form.cleaned_data['password'])

            # commit the changed to the database
            new_user.save()

            # log in new user
            django_login(request, new_user)

            return redirect('shop_app:register')

    
    context = {
        'form': form
    }

    return render(request, 'users/register.html', context)


def login(request):
    if request.method == 'GET':
        form = UserAuthForm()
        context = {
            'form': form
        }
        return render(request, 'users/login.html', context)

    elif request.method == 'POST':

        # get the form data from the http request
        form = request.POST

        # get the values from the form
        username = form.get('username')
        password = form.get('password')


        # attempt to authenticate the user
        user = authenticate(request, username=username, password=password)

        # if the form credentials are not valid, 
        # render the login page
        if user is None:
            # add an error message to the messages api
            messages.error(request, 'Invalid username or password!')

            context = {
                'form': UserAuthForm()
            }
            return render(request, 'users/login.html', context)

        # login the authenticated user
        django_login(request, user)

        return redirect('shop_app:index')


@login_required
def list_users(request):
    # grab all the users from the database
    users = get_user_model().objects.all()

    context = {
        'users': users
    }

    return render(request, 'users/list.html', context)


@login_required # redirects to login page if request.user.is_authenticated is False
def detail(request, username):

    # use the get_user_model function to find the current User model
    user = get_object_or_404(get_user_model(), username=username)

    context = {
        'user': user,
        'products': Product.objects.all()[:5]
    }

    return render(request, 'users/detail.html', context)


def update(request, username):
    # get the user from the database
    user = get_object_or_404(get_user_model(), username=username)
    

    if request.method == 'GET':
        form = UserForm(instance=user)

        context = {
            'form': form
        }

        return render(request, 'users/update.html', context)

    elif request.method == 'POST':
        # create a UserForm with the form data 
        # and the User instance to which to apply the changes
        form = UserForm(request.POST, instance=user)

        # grab the uploaded image file from the HTML form
        new_avatar = request.FILES.get('avatar')


        # if a file was uploaded, add it to the form fields
        if new_avatar:
            form.initial['avatar'] = new_avatar

        # if the form is valid, update the user instance
        if form.is_valid():
            form.save()

            # redirect to the user detail page,
            # providing the username as a kwarg using the reverse() function
            return redirect(reverse('users_app:detail', args=[user.username]))

        else:
            context = {
                'form': form
            }
            return render(request, 'users/update.html', context)


@login_required
def follow(request, username):

    # get the user from the database
    user = get_object_or_404(get_user_model(), username=username)

    # if the requesting user is not already in the list of followers
    # add the user who made the request to the followers list
    # of the user object from the db. If they are in the list, remove them
    if request.user not in user.followers.all():
        user.followers.add(request.user)

    else:
        user.followers.remove(request.user)


    return redirect('users_app:list')

def logout(request):
    django_logout(request)

    return redirect('users_app:login')


