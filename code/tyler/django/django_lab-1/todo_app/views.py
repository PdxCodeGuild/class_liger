from django.shortcuts import render, redirect
from django.urls import reverse
from models import Priority, TodoItem, models
# Create your views here.


def index(request):
    todos = TodoItem.objects.all()
    context = {
        'todos': todos
    }

    return render(request, 'index.html', context)


def save_todo_item(request):
    form = request.POST
    priority_item = form.get('priority_name')
    list_item = form.get('todo_text')
    todos = TodoItem.objects.create(text=list_item)
    return redirect(reverse('todo_app:index'))
