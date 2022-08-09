from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')

def JS_Lab_1(request):
    return render(request, 'pages_app/JS_Lab_1.html')

def JS_Lab_2(request):
    return render(request, 'pages_app/JS_Lab_2.html')

def JS_Lab_3(request):
    return render(request, 'pages_app/JS_Lab_3.html')