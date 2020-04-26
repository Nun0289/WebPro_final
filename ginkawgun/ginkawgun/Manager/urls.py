from django.urls import path
from . import views
urlpatterns = [
    path('food_detail/', views.app_food_detail,name='food_detail'),
    path('addfood/',views.app_add_food, name='add_food'),
]