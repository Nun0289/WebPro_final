from django.contrib.messages.storage import session
from django.http import HttpResponse
from django.shortcuts import render

from Manager.models import Menu
from User.models import Customer


# Create your views here.
def app_homepage(request):
    menu_all = Menu.objects.all()
    user_all = Customer.objects.all()
    customer = Customer.objects.get(user=request.user)
    request.session['phone'] = customer.nphone
    context = {
        'menu_all': menu_all,
        'user_all': user_all
    }
    return render(request, template_name='home.html', context=context)
def app_food_detail(request):
    return render(request, template_name='food_detail.html')
def app_add_food(request):
    return render(request, template_name='add_food.html')
