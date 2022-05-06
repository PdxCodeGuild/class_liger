from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import UserForm, UserAuthForm
# Create your views here.
from django.contrib.auth import (
    login as django_login,
    logout as django_logout,
    authenticate,
    get_user_model 
)

def base_view(request):

    # context = {

    # }

    return render(request, 'user_app/base.html')

# --------------------------------------------------------
    
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

            return redirect('users_app:profile')

    
    context = {
        'form': form
    }

    return render(request, 'user_app/register.html', context)
    # form = request.POST

    # print(request.POST)

    # for key in form:

    #     if key.startswith('username'):

    #         name = form.get(key)

    #         CustomUser.objects.create(username=name)
    
    # for key in form:

    #     if key.startswith('email'):

    #         contact = form.get(key)

    #         CustomUser.objects.create(email=contact)

        

    # return render(request, 'user_app/profile.html')

# --------------------------------------------------------

def login(request):

    return render(request, 'user_app/login.html')

# --------------------------------------------------------

def profile(request):

    return render(request, 'user_app/profile.html')

# --------------------------------------------------------