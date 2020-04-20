from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vendor(models.Model):
    address = models.TextField()

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Customer(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)