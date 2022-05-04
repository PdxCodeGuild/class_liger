





from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo, Priority
from django.urls import reverse
# Create your views here.

def main_view(request):

    todos = Todo.objects.all()

    priority = Priority.objects.all()

    context = {

        'todos' : todos,
        'priority' : priority
    }
    return render(request, 'todo_app/base.html', context)

# --------------------------------------------------------------------   

# def list_todos(request):

#     todos = Todo.objects.all()

#     priority = Priority.objects.all()

#     context = {

#         'todos' : todos,
#         'priority' : priority
#     }

#     return render(request, 'todo_app/todos.html', context)

# -----------------------------------------------------------

def save_todo_items(request):

    form = request.POST

    print(request.POST)

    todos = Todo.objects.all()

    priority = Priority.objects.all()

    context = {

        'todos' : todos,
        'priority' : priority
    }

    # item_text = form.get('text')
    # # todo_id = form.get('todo-id')
    # list_item = Todo.objects.create(text=item_text)
    # list_item.save
    for key in form:

        if key.startswith('text'):

            task_text = form.get(key)

            Todo.objects.create(text=task_text)
        
    for key in form:
        if key.startswith('name'):

            prio = form.get(key)

            Priority.objects.create(name=prio)

    # task = get_object_or_404(Todo)
    # task.text = new_task
    # task.save
    return render(request, 'todo_app/base.html', context)

# ------------------------------------------------------------

def list_todos(request):
    
    todos = Todo.objects.all()

    context = {

        'todos' : todos,
    }

    return render(request, 'todo_app/list_todos.html', context)

# ----------------------------------------------------------------

