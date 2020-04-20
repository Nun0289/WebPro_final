from django.contrib import admin
from .models import Type,Restaurant,Order,Order_list,feedback,Menu
# Register your models here.
admin.site.register(Type)
admin.site.register(Restaurant)
admin.site.register(Order)
admin.site.register(Order_list)
admin.site.register(feedback)
admin.site.register(Menu)