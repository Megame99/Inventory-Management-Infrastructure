
# Create your models here.

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(blank=True) 
    code = models.PositiveIntegerField(unique=True)
    manufacturer_price = models.DecimalField(max_digits=10, decimal_places=2)


class Item(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(blank=True) 
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=200)
    itemcode = models.PositiveIntegerField(unique=True)

    class Meta:
        db_table = "inventory"


class Order(models.Model):
    item= models.ForeignKey(Item,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    orderID = models.PositiveIntegerField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    destination = models.CharField(max_length=200)
    item_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2,blank=True)

class Shipment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    ship_cost = models.DecimalField(max_digits=10,decimal_places=2)   
    duration = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    shipId = models.PositiveIntegerField(unique=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
        

