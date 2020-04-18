from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app_homepage(request):
    return render(request, template_name='home.html')
def app_food_detail(request):
    return render(request, template_name='food_detail.html')