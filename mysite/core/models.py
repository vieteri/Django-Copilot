from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    """ a model that has a name, description, price and the date it was created as well as well as a status field """
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    """ A model that represents purchases of items with a purchase date and whether or not it was shipped """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    purchaser = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='1')
    purchase_date = models.DateTimeField(auto_now_add=True)
    shipped = models.BooleanField(default=False)
    def __str__(self):
            return self.item.name

class ItemCollection(models.Model):
    """ A collection of multiple items connected to a user """
    items = models.ManyToManyField(Item)

    def __str__(self):
        return self.user.username
    