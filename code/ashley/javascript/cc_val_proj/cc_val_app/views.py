from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ccVal(request):
    return HttpResponse('hello world!')