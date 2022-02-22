from typing import ItemsView
from django import forms 
from inventory.models import Item, Shipment, Order

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['quantity', 'retail_price', 'description',]

class ShipmentForm(forms.ModelForm):
    class Meta:
        model=Shipment
        fields=['destination',]

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['quantity', 'destination', 'email',]