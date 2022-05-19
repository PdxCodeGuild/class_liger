from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'blog_app/index.html', context)

def register(request):

    return render(request, 'auth/profile.html')

def login(request):

    return render(request, 'auth/profile.html')

def profile(request):
    context = {
        'message': 'Hi! Welcome to your profile.'
    }
    return render(request, 'auth/user_profile.html', context)