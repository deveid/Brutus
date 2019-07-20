from django.db import models
from .forms import User
# Create your models here.
class ShoppingList(models.Model):
    """MOdel for a single shoppinglist"""
    name=models.CharField(max_length=12,null=False)
    owner=models.ForeignKey('User',related_name='shopping_lists',
    on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now=True)
    date_updated=models.DateField(auto_now=True)

    class Meta:
        ordering=('-date_created')

class ShoppingItem(models.Model):
    name=models.CharField(max_length=12, null=False)
    quantity=models.DecimalField(default=0.00, decimal_places=2)
    price=models.DecimalField(default=0.00, decimal_places=2)
    list=models.ForeignKey(ShoppingList, related_name='shopping_items',
    on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-date_created')

