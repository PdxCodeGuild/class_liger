from rest_framework import serializers

from .models import GroceryItem

class GroceryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryItem
        
        # include all fields
        fields = '__all__'

        # OR

        # specify a list of fields
        # fields = ['name', 'quantity']


class GroceryItemCreateSerializer(GroceryItemSerializer):
    class Meta(GroceryItemSerializer.Meta):
        fields=['name', 'quantity']