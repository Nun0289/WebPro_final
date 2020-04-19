from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
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

class Menu(models.Model):
    name = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()

class Order(models.Model):
    total_price = models.FloatField()
    payment = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)

class Order_list(models.Model):
    unit = models.IntegerField()
    description = models.TextField()
    unit_price = models.FloatField()


class feedback(models.Model):
    date = models.DateField(auto_now_add=True)
    description = models.TextField()