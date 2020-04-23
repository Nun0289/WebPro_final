from django.contrib import admin
from .models import Type,Restaurant,Order,Order_list,feedback,Menu
# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name','picture','address','time','phone','type_id']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['total_price','payment','datetime']
class Order_listAdmin(admin.ModelAdmin):
    list_display = ['unit','description','description','unit_price','order']
class feedbackAdmin(admin.ModelAdmin):
    list_display = ['date','description','vendor','customer']
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name','picture','price','description','restaurant']

admin.site.register(Type,TypeAdmin)
admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Order_list,Order_listAdmin)
admin.site.register(feedback,feedbackAdmin)
admin.site.register(Menu,MenuAdmin)