from django.shortcuts import render

# Create your views here.
def phrase(request):
    return render(request, 'phrase.html')


def unitconverter(request):
    return render(request, 'unitcont.html')


def todolist(request):
    return render(request, 'todolist.html')


def passwordgent(request):
    return render(request, 'passwordgent.html')