

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
    path('edituser_form/<int:user_id>',views.edituser_form,name='edituser_form')
]
