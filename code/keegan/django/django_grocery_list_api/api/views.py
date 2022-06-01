from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from grocery_app.models import GroceryItem
from grocery_app.serializers import GroceryItemSerializer

@api_view(['GET'])
def grocery_list(request):
    # create a blank JSON response
    response = Response()

    # get all the GroceryItems
    grocery_items = GroceryItem.objects.all()

    # serialize the queryset
    # many=True will allow multiple instances of GroceryItem
    serialized_items = GroceryItemSerializer(grocery_items, many=True)

    # attach the serialized items to the response object
    response.data = {
        'groceryItems': serialized_items.data
    }


    return response
