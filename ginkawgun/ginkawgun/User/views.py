from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def app_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            print("OK")
            return redirect('homepage')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password'

    return render(request, template_name='login.html',context=context) 

def app_register(request):
    return render(request, template_name='register.html')
