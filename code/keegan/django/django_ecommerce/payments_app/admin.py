from django.contrib import admin

from .models import Receipt, ReceiptItem


class ReceiptItemInline(admin.TabularInline):
    model=ReceiptItem
    fields=['product_name', 'item_price', 'quantity']
    readonly_fields=['product_name', 'item_price']

    def product_name(self, receipt_item):
        return receipt_item.product.title

    def item_price(self, receipt_item):
        return receipt_item.product.price * receipt_item.quantity

class ReceiptAdmin(admin.ModelAdmin):
    fields=['purchase_date', 'total_price']
    readonly_fields=['purchase_date', 'total_price']

    # inlines are used to represent database relationships in the admin panel
    inlines=[ReceiptItemInline]

    def total_price(self, receipt):
        return f"${receipt.total_price()}"

admin.site.register(Receipt, ReceiptAdmin)