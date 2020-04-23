from django.urls import path,include
from . import views
urlpatterns = [
    path('edituser_form/',views.edituser_form,name='edituser_form')
]