from django.shortcuts import render
from .models import TodoItem, models
from django.urls import reverse
from django.shortcuts import redirect
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
    print(form)

    list_item = form.get('todo-text')
    todos = TodoItem.objects.create(text = todo_text)
    context = {
        'todos' : todos,
    }
    return redirect(reverse('todo_app:index'))

