from lib2to3.fixes.fix_input import context
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, template_name='register.html')