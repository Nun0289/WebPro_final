from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('edituser/',app_useredit,name='edituser')
]