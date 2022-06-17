from core.models import Item, Purchase
from django.contrib.auth.models import User

from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    """ a serializer for the Item model """
    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'price', 'created_at', 'status')

class PurchaseSerializer(serializers.ModelSerializer):
    """ a serializer for the Purchase model """

    item = ItemSerializer(read_only=True)
    class Meta:
        model = Purchase
        fields = ('id', 'item', 'purchase_date', 'shipped')