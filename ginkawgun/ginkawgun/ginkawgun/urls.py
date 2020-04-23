"""ginkawgun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from User import views as user_views
from Manager import views as manager_views
urlpatterns = [
    path('login/',user_views.app_login,name='login'),
    path('logout/',user_views.app_logout,name='logout'),
    path('register/',user_views.app_register,name='register'),
    path('admin/', admin.site.urls ,name='admin'),
    path('food_detail/', manager_views.app_food_detail,name='food_detail'),
    path('',manager_views.app_homepage, name='homepage'),
    path('addfood/',manager_views.app_add_food, name='add_food'),
    path('edituser/',user_views.app_useredit,name='edituser')
]
