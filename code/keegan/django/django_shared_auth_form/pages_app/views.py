from django.shortcuts import render


def register(request):
    context = {
        'form_mode': 'register'
    }
    return render(request, 'auth-form.html', context)


def login(request):
    context = {
        'form_mode': 'login'
    }
    return render(request, 'auth-form.html', context)