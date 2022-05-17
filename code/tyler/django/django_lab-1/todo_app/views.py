from django.shortcuts import render, redirect
from django.urls import reverse
from .models import TodoItem, models
# Create your views here.


def index(request):
    todos = TodoItem.objects.all()
    print(todos)
    context = {
        'todos': todos
    }

    return render(request, 'index.html', context)


def save_todo_item(request):
    form = request.POST
    print("request post", request.POST)
    list_item = form.get('todo_text')
    print("TEST", list_item)
    todos = TodoItem.objects.create(text=list_item)
    print(todos)
    return redirect(reverse( 'todo_app:index'))
