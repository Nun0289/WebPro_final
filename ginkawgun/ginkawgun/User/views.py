from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app_login(request):
    return render(request, template_name='login.html')
def app_register(request):
    return render(request, template_name='register.html')