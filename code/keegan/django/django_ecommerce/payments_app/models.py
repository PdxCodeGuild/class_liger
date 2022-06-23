from django.db import models
from django.contrib.auth import get_user_model
from shop_app.models import Product

class ReceiptItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='receipt_items')
    receipt = models.ForeignKey('Receipt', on_delete=models.CASCADE, related_name='receipt_items')
    quantity = models.IntegerField(default=1)

    def item_subtotal(self):
        '''return the total price of a ReceiptItem'''
        return self.quantity * self.product.price

class Receipt(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='receipts')

    purchase_date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through=ReceiptItem, related_name='receipts')

    def total_price(self):
        total = 0
        for receipt_item in self.receipt_items.all():
            total += receipt_item.item_subtotal()

        return total

    def __str__(self):
        return f"{self.user} | {self.purchase_date.strftime('%Y-%m-%d')} | ${self.total_price()}"