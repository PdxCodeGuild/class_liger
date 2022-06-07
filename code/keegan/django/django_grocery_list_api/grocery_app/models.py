from django.db import models

# GroceryItem

class GroceryItem(models.Model):
    # fields

    # name - string
    name = models.CharField(max_length=255)

    # quantity - integer
    quantity = models.PositiveIntegerField(default=1)

    # price - decimal
    # price = models.DecimalField(decimal_places=2, max_digits=10)

    # in_cart - boolean
    in_cart = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + str(self.quantity)