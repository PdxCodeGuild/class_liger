# from audioop import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Priorities, TodoItem


def index(request):
    # return HttpResponse("Hello World")
    # context = {"message": "Hello!!!!"}
    to_do_items = TodoItem.objects.filter(created_date__lte=timezone.now()).order_by(
        "-created_date"
    )

    to_do_complete = to_do_items.filter(task_complete=True)
    to_do_incomplete = to_do_items.filter(task_complete=False)

    context = {
        "to_do_items": to_do_items,
        "to_do_complete": to_do_complete,
        "to_do_incomplete": to_do_incomplete,
    }

    return render(request, "layout/index.html", context)
    # return render(request, "layout/index.html", context)


def create(request):
    form = request.POST
    # new_to_do = form.get("create")
    # new_to_do_item = TodoItem.objects.create(text=new_to_do)
    # return redirect("to_do_app:create")

    description = form["create"]
    selected_priority = form["priority-rank"]

    # Priorities.objects.get_or_create(setting=selected_priority)

    # TodoItem.objects.create(
    #     text=description,
    #     created_date=timezone.now(),
    #     # task_complete=False,
    # )

    created, prioritized = Priorities.objects.get_or_create(setting=selected_priority)
    TodoItem.objects.create(text=description, priority=created)

    return HttpResponseRedirect(reverse("to_do_app:index"))


def delete(request, to_do_item_id):
    donetodo = TodoItem.objects.get(id=to_do_item_id)

    donetodo.delete()

    return redirect("to_do_app:index")
