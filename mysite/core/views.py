from django.shortcuts import render
from django.template import RequestContext
from .models import Item, Purchase
import requests
from django.views.decorators.csrf import csrf_protect
from django.template.context_processors import csrf
# Create your views here.

data = {
    'items': ''
}


def index(request):
    """ a list of all items in the database """
    data['items'] = Item.objects.all()
    if request.user.is_authenticated:
        data['user'] = request.user.username
    else:
        data['user'] = 'not authenticated'
    return render(request, 'core/index.eta', data)

def detail(request, item_id):
    """ a detail view of an item """
    item = Item.objects.get(id=item_id)
    return render(request, 'core/detail.html', {'item': item})





@csrf_protect
def UserView(request):
    """ a list of all items in the database """
    #Filter by user
    data['purchases'] = Purchase.objects.filter(purchaser=request.user)
    #data['items'] = Item.objects.all()
    #fetch data['items'] from rest api http://localhost:8000/api/items/?format=api
    ItemList = requests.get('http://localhost:8000/api/items/?format=json')
    data['items'] = ItemList.json()
    #print(data['items'].content)
    if request.user.is_authenticated:
        data['user'] = request.user.username
    else:
        data['user'] = 'not authenticated'
    
    # Add CSRF token
    c = {}
    c.update(csrf(request))
    data.update(c)
    
    return render(request, 'core/purchase.eta', data)
