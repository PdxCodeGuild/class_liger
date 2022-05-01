





from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo, Priority
from django.urls import reverse
# Create your views here.

def main_view(request):

    context = {

    }
    return render(request, 'todo_app/base.html')

def list_todos(request):

    todos = Todo.objects.all()

    priority = Priority.objects.all()

    context = {

        'todos' : todos,
        'priority' : priority
    }

    return render(request, 'todo_app/base.html', context)

def add_todo(request):

    form = request.POST

    todo_id = form.get('todo-id')

    todo = Todo.objects.get(id=todo_id)

    return redirect(reverse('todo_app:base'))



    