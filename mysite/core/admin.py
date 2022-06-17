from django.contrib import admin
from .models import Item, ItemCollection, Purchase
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at', 'status')
    search_fields = ('name',)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('item', 'purchase_date', 'shipped')
