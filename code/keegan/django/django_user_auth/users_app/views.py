from django.shortcuts import render

from .models import User

def register(request):

    # when arriving at the page, render the register form
    if request.method == 'GET':
        return render(request, 'auth/register.html')

    # process the form once it is submitted
    elif request.method == 'POST':
        # grab the data from the HTML form
        form = request.POST

        username = form.get('username')
        password = form.get('password')

        # create_user() is used instead of create()
        # for users so the password gets hashed
        new_user = User.objects.create_user(
            username=username,
            password=password
        )

        return render(request, 'auth/register.html')