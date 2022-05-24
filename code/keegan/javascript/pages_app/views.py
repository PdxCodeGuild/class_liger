from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def events_demo_1(request):
    return render(request, 'events-demo-1.html')

def events_demo_2(request):
    return render(request, 'events-demo-2.html')

def async_demo_1(request):
    return render(request, 'async-demo-1.html')

def async_demo_2(request):
    return render(request, 'async-demo-2.html')

