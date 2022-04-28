from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import (
    authenticate, 
    # change the names of login and logout to
    # avoid a naming conflict with the views
    login as django_login,
    logout as django_logout
)

# from django.http import Http404

# middleware for adding messages to templates
from django.contrib import messages

from .models import User

def register(request):

    # when arriving at the page, render the register form
    if request.method == 'GET':
        return render(request, 'auth/register.html')

    # process the form once it is submitted
    elif request.method == 'POST':
        # grab the data from the HTML form
        form = request.POST

        # grab the username and password from the form
        username = form.get('username')
        password = form.get('password')

        # create_user() is used instead of create()
        # for users so the password gets hashed
        new_user = User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, f'Welcome, {new_user.username}')

        django_login(request, new_user)

        return redirect('polls_app:index')


def login(request):

    # render the login form when arriving at the page with a GET request
    if request.method == 'GET':
        return render(request, 'auth/login.html')

    # process the form once it is submitted with a POST request
    elif request.method == 'POST':

        # grab the form from the HTTP request
        form = request.POST

        # grab the username and password from the form
        username = form.get('username')
        password = form.get('password')


        # try to authenticate the user with the credentials from the form
        # authenticate() returns either the user, if credentials are valid or None
        user = authenticate(request, username=username, password=password)


        # if the user was not authenticated,
        # render the login form with an error
        if user is None:
            # add a message to the request
            messages.error(request, 'Invalid Username or Password!')
            # render login form
            return render(request, 'auth/login.html')

        # if the user was authenticated, log them in
        django_login(request, user)

        # add a success message to the request
        messages.success(request, f'Welcome {user.username}!')

        return redirect('polls_app:index')


def logout(request):
    # logout the user
    django_logout(request)

    return redirect('polls_app:index')


def detail(request, username):

    # try:
    #     # use the username to find the appropriate user in the database
    #     user = User.objects.get(username=username)

    # except User.DoesNotExist:
    #     raise Http404('"No User matches the given query."')

    # return the user object if found, otherwise raise 404 error
    user = get_object_or_404(User, username=username)

    context = {
        'user': user,
    }

    return render(request, 'users/detail.html', context)