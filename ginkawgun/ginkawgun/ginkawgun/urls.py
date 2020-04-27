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
from django.conf import settings
from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from Manager import views as manager_views
from User import views as user_views

urlpatterns = [
    path('login/',user_views.app_login,name='login'),
    path('logout/',user_views.app_logout,name='logout'),
    path('register/',user_views.app_register_from,name='register'),
    path('admin/', admin.site.urls ,name='admin'),
    path('cpass/',user_views.app_changepass,name='cpass'),
    path('',manager_views.app_homepage, name='homepage'),
    path('', include('User.urls')),
    path('',include('Manager.urls')),
    path('addfood/',manager_views.app_add_food, name='add_food'),
    path('foodupdate/',manager_views.app_update_food, name='update_food'),
    path('menuupdate/<int:menu_id>/',manager_views.menu_update, name='menu_update'),
    path('menudelete/<int:menu_id>/',manager_views.menu_delete, name='menu_delete'),
    path('add_to_cart/<int:menu_id>/',manager_views.add_cart, name='addtocart'),
    path('delete_order/<int:order_id>/', manager_views.delete_order, name='delete_order'),
    path('plus_order/<int:order_id>/', manager_views.plus_order, name='plus_order'),
    path('minus_order/<int:order_id>/', manager_views.minus_order, name='minus_order'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
