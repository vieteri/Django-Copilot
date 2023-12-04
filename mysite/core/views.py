from django.shortcuts import render
from .models import Item
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