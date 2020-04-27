from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('food_detail/', views.app_food_detail,name='food_detail'),
    path('addfood/',views.app_add_food, name='add_food'),
    path('menu/<int:res_id>/', views.menu_list, name='menu'),
    path('order/<int:res_id>/', views.order, name='order'),
    path('updatecart/',views.update_cart, name='updatecart'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
