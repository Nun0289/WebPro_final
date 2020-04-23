from django.db import models
from User.models import Vendor, Customer

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % (self.name)

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='restaurant_image', blank=True)
    address = models.TextField()
    time = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '(%s) %s' % (self.type_id.name, self.name)

class Menu(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='menu_image', blank=True)
    price = models.FloatField()
    description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '(%s) %s %d %s' % (self.restaurant.name, self.name, self.price, self.description)

class Order(models.Model):
    total_price = models.FloatField()
    payment = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.total_price, self.payment)

class Order_list(models.Model):
    unit = models.IntegerField()
    description = models.TextField()
    unit_price = models.FloatField()

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '(%s) %s %s %s' % (self.order.id, self.unit, self.description, self.unit_price)
class feedback(models.Model):
    date = models.DateField(auto_now_add=True)
    description = models.TextField()

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '(%s) (%s) %s' % (self.vendor.user.username, self.customer.fname, self.description)

