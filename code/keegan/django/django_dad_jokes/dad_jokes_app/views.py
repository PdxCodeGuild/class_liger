from django.shortcuts import render
import requests

# basic HTTP Response
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello world!")
    # return HttpResponse("<h1>Hello world!</h1>")
    return render(request, 'dad_jokes_app/index.html')


def jokes_list(request):

    url = "https://icanhazdadjoke.com/search"

    headers = {
        'accept': 'application/json'
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    # wrap the response data in the context dictionary
    context = {
        'jokes_list': data['results']
    }

    return render(request, 'dad_jokes_app/jokes.html', context)