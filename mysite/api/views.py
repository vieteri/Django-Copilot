from django.shortcuts import render
from core.models import Item, Purchase
from .serializers import ItemSerializer, PurchaseSerializer
from rest_framework import viewsets
# Create your views here.

class PurchaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows purchases to be viewed or edited.
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
