from django.db import models
from User.models import Vendor, Customer

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=255)

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    address = models.TextField()
    time = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return '(%s) %s' % (self.type_id.name, self.name)

class Order(models.Model):
    total_price = models.FloatField()
    payment = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)

class Order_list(models.Model):
    unit = models.IntegerField()
    description = models.TextField()
    unit_price = models.FloatField()

    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class feedback(models.Model):
    date = models.DateField(auto_now_add=True)
    description = models.TextField()

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Menu(models.Model):
    name = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()

    order_list = models.ForeignKey(Order_list, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)