from webbrowser import register

from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Customer, Vendor

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['','','','']

admin.site.register(Permission)
admin.site.register(Customer)
admin.site.register(Vendor)