from lib2to3.fixes.fix_input import context
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.
def app_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request,user)
            return redirect('homepage')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password'

    return render(request, template_name='login.html',context=context)

def app_logout(request):
    logout(request)
    return redirect('login')

def app_register(request):
    context = {}
    print("1")
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('cpassword')
        print(password)
        print(password2)
        if password == password2:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            print("OK")
            return redirect('login')
        else:
            context['error'] = 'Password Not Match!!!'
            return render(request, template_name='register.html', context=context)
            print("NO")
    
    return render(request, template_name='register.html', context=context)