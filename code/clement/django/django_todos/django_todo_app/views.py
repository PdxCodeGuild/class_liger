from multiprocessing import context
from django.shortcuts import render, reverse
from django.urls import reverse

from django.http import HttpResponseRedirect


# Create your views here.
from .models import Priority, TodoItem

def index(request):
    priority = Priority.objects.all()
    todoitem = TodoItem.objects.all()

    context = {
        'priority': priority,
        'todoitem': todoitem
    }
    return render(request, 'index.html', context)

# This page is going to the all the todo items.
def save_todo_item(request):
    form = request.POST
    print(form)

# create todoitem from form
    priority_text = form.get('priority-text')
    todoitem_text = int(form.get('todoitem-text'))


# save todoitem


# redirect back to the index page
    return HttpResponseRedirect(reverse('myapp:index'))
