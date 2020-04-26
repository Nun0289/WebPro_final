from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('edituser_form',views.edituser_form,name='edituser_form')
]