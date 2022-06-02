from cmath import pi
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from grocery_app.models import GroceryItem
from grocery_app.serializers import GroceryItemSerializer, GroceryItemCreateSerializer

@api_view(['GET'])
def grocery_retrieve(request, grocery_item_id=None):
    # create a blank JSON response
    response = Response()


    # serialize all grocery items if no grocery_item_id is passed
    if not grocery_item_id:
        # get all the GroceryItems
        grocery_items = GroceryItem.objects.all()

        # serialize the queryset
        # many=True will allow multiple instances of GroceryItem
        serializer = GroceryItemSerializer(grocery_items, many=True)

    # find and serialize the single item
    else:
        # use the grocery_item_id to find the desired item
        # .first() will either return the first item of the queryset, if it exists, 
        # or return None if it doesn't
        grocery_item = GroceryItem.objects.filter(id=grocery_item_id).first()

        if grocery_item:
            # serialize the single grocery item
            serializer = GroceryItemSerializer(grocery_item)

            # attach the serialized items to the response object
            response.data = {
                'groceryItems': serializer.data
            }
        else:
            # set the serializer data to an error message and error status code
            response.data = {
                'error': f'GroceryItem with id {grocery_item_id} not found!'
            }
            # set the status code to 404
            response.status_code = status.HTTP_404_NOT_FOUND

    return response



@api_view(['POST'])
def grocery_create(request):
    response = Response()

    data = request.data

    # initialize the serializer with the data from the request
    serializer = GroceryItemCreateSerializer(data=response.data)

    print(serializer.initial_data)


    # check if the request data is valid for creating a new object
    if serializer.is_valid():
        message = 'valid'
    else:
        message = serializer.errors

    response.data = {
        'message': message
    }

    return response

    