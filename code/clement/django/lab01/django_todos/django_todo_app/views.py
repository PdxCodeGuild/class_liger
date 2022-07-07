from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
from .models import Priority, TodoItem


def index(request):
    # priority = Priority.objects.all()
    todoitems = TodoItem.objects.all()

    context = {
        # 'priority': priority,
        'todoitem': todoitems
    }
    return render(request, 'index.html', context)

# This page is going to the all the todo items.


def save_todo_item(request):
    form = request.POST
    print(form)

# create todoitem from form 
    priority_text = form.get('priority-text')
    todoitem_text = form.get('todo-text')



# Use the priority-text from the form to get_or_create the item from the Priority table with that text.

    priority, created = Priority.objects.get_or_create(text=priority_text)
       
#create a TodoItem using the todoitem-text from the form and associate it with the Priority object from the previous step
    todoitem = TodoItem.objects.create(text=todoitem_text, priority=priority)



    # save todoitem & priority
    # priority_text.save()
    # todoitem_text.save()

    # redirect back to the index view/page
    return redirect(reverse('django_todo_app:index'))
