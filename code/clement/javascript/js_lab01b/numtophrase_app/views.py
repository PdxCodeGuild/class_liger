from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def phrase(request):
    return render(request, 'phrase.html')