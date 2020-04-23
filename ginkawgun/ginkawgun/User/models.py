from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vendor(models.Model):
    address = models.TextField()

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=True)

    def __str__(self):
        return '%s' % (self.user.username)

class Customer(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    nphone = models.CharField(max_length=10, null=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=True)

    def __str__(self):
        return '(%s) %s %s %d' % (self.user.username, self.fname, self.lname, self.phone)