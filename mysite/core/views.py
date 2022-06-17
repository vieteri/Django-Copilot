from django.shortcuts import render
from .models import Item
# Create your views here.

def index(request):
    """ a list of all items in the database """
    items = Item.objects.all()
    return render(request, 'core/index.html', {'items': items})

def detail(request, item_id):
    """ a detail view of an item """
    item = Item.objects.get(id=item_id)
    return render(request, 'core/detail.html', {'item': item})