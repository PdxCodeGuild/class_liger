from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect

from .models import Priority, TodoItem

# Create your views here.
def index(request):
    todo_items = TodoItem.objects.all()
    context = {
        'TodoItems': todo_items
    }
    return render(request, 'todo/index.html', context)

def add_item(request):
    
    if request.method=="POST":

        form = request.POST

        print('form', form)
        print('new-task', form.get('new-task'))

        new_task = form.get('new-task')

        priority_text = form.get('priority')
        print(priority_text)

        new_task = TodoItem(text=new_task)

        priority, created = Priority.objects.get_or_create(priority=priority_text)

        new_task.priority = priority

        new_task.save()

        context = {
            'TodoItems': new_task
        }
        # return render(request, 'todo/add-item.html', context)

        return redirect(reverse('todo_app:index'))
        
    else:
        return render(request, 'todo/add-item.html')