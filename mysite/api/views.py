from django.shortcuts import render
from core.models import Item, Purchase
from .serializers import ItemSerializer, PurchaseSerializer
from rest_framework import viewsets
from rest_framework import permissions
# Create your views here.


class PurchaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows purchases to be viewed or edited.
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add this line
    def perform_create(self, serializer):
        serializer.save(purchaser=self.request.user)


class PurchaseUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows purchases to be viewed or edited of the current user   
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]  # Add this line
    def get_queryset(self):
        user = self.request.user
        return Purchase.objects.filter(purchaser=user)
    def perform_create(self, serializer):
        serializer.save(purchaser=self.request.user)

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
