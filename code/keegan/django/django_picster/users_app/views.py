from django.shortcuts import render, redirect
from .forms import UserAuthForm
from django.contrib.auth import login as django_login, logout as django_logout


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

            return redirect('users_app:register')

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def logout(request):
    django_logout(request)

    return redirect('users_app:register')