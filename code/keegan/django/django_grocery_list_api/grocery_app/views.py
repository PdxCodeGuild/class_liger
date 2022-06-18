from django.shortcuts import render, redirect, get_object_or_404

from .models import GroceryItem

def grocery_list(request):

    groceries = GroceryItem.objects.all().order_by('in_cart')

    context = {
        'groceries': groceries
    }

    return render(request, 'index.html', context)


def add_item(request):

    form = request.POST

    new_item_name = form.get('new-item-name')
    new_item_quantity = form.get('new-item-quantity')
    
    GroceryItem.objects.create(
        name=new_item_name,
        quantity=new_item_quantity
    )

    return redirect('grocery_app:grocery_list')


def toggle_cart_status(request, grocery_item_id):
    # get the item from the database
    grocery_item = get_object_or_404(GroceryItem, id=grocery_item_id)

    # toggle the item's in_cart value
    grocery_item.in_cart = not grocery_item.in_cart

    # save the item
    grocery_item.save()

    return redirect('grocery_app:grocery_list')


def delete_item(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, id=grocery_item_id)

    grocery_item.delete()

    return redirect('grocery_app:grocery_list')


def increment_quantity(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, id=grocery_item_id)

    grocery_item.quantity += 1

    grocery_item.save()
    
    return redirect('grocery_app:grocery_list')


def decrement_quantity(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, id=grocery_item_id)

    grocery_item.quantity -= 1

    grocery_item.save()
    
    return redirect('grocery_app:grocery_list')