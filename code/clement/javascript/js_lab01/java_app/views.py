from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'navbar.html')
def phrase(request):
    return render(request, 'phrase.html')


def unitconverter(request):
    return render(request, 'unitcont.html')


def todo(request):
    return render(request, 'todo.html')

def passwordgent(request):
    return render(request, 'passwordgent.html')