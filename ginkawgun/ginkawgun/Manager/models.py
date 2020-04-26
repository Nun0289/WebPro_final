from django.db import models
from User.models import Vendor, Customer

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='restaurant_image', blank=True)
    address = models.TextField()
    time = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    food = 'ร้านอาหาร'
    drink = 'ร้านเครื่องดื่ม'
    res_type = (
        (food, 'food'),
        (drink, 'drink')
    )
    restaurant_type = models.CharField(
        max_length = 15,
        choices = res_type,
        default=food
    )

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s' % (self.name)

    
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
    unit = models.IntegerField(default=1)
    unit_price = models.FloatField(default=False)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s %s' % (self.total_price, self.payment)

class feedback(models.Model):
    date = models.DateField(auto_now_add=True)
    description = models.TextField()

    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '(%s) (%s) %s' % (self.vendor.user.username, self.customer.fname, self.description)