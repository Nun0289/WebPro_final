from django.contrib.messages.storage import session
from django.http import HttpResponse
from django.shortcuts import render

from Manager.models import *
from User.models import *
from django.contrib.auth.decorators import login_required


def app_homepage(request):
    search = request.GET.get('search', '')
    res_list = Restaurant.objects.all()
    user_all = Customer.objects.all()
    customer = Customer.objects.get(user=request.user)
    menu_list = Menu.objects.all()
    request.session['phone'] = customer.nphone
    if search != '':
        menu_list = Menu.objects.filter(name__icontains=search)

    context = {
        'res_list': res_list,
        'user_all': user_all,
        'menu_list': menu_list
    }
    return render(request, template_name='home.html', context=context)

def menu_list(request, res_id):
    res = Restaurant.objects.get(pk=res_id)
    menu_list = Menu.objects.filter(restaurant__id=res_id)
    context = {
        'res': res,
        'menu_list': menu_list,
    }

    return render(request, template_name='menu.html', context=context)

def order(request, res_id):
    current_user = request.user
    res = Restaurant.objects.get(pk=res_id)
    order = Order.objects.filter(restaurant__id=res_id)
    # if current_user == restaurant.vendor.user_id:

    return render(request, template_name='order.html', context={
        'order': order,
        'res': res,
    })

def app_food_detail(request):
    return render(request, template_name='food_detail.html')
def app_add_food(request):
    return render(request, template_name='add_food.html')
