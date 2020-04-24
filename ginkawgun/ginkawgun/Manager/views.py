from django.shortcuts import render
from django.http import HttpResponse
from Manager.models import Menu
from User.models import Customer
# Create your views here.
def app_homepage(request):
    menu_all = Menu.objects.all()
    user_all = Customer.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'menu_all': menu_all,
        'user_all': user_all,
        'num_visits':num_visits
    }
    return render(request, template_name='home.html', context=context)
def app_food_detail(request):
    return render(request, template_name='food_detail.html')
def app_add_food(request):
    return render(request, template_name='add_food.html')