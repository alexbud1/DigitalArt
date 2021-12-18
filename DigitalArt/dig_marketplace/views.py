from django.contrib.auth import login
from .forms import *
from django.shortcuts import  render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

def login_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        error = ''
        if request.method == "POST":
            username = request.POST.get('email')
            password = request.POST.get("password1")
            user = authenticate(request, email=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                error = "Не верное имя пользователя или пароль"
                context = {'error':error}
                return render(request, 'dig_marketplace/login.html',context)
        context = {'error':error}
    return render(request, 'dig_marketplace/login.html')

def logout_page(request):
    logout(request)
    return redirect('login')


def signup_page(request):
    form = CustomUserCreationForm()
    context = {'form': form}

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.month_joined= datetime.now().strftime('%B')
            user.day_joined= datetime.now().day
            user.year_joined= datetime.now().year
            user.save()
            print(datetime.now().day)
            ###### redirect works with name in urls.py
            return redirect('homepage')
    return render(request, 'dig_marketplace/sign_up.html', context)

def homepage(request):
    return render(request, 'dig_marketplace/homepage.html')

def account_page(request):
    return render(request, 'dig_marketplace/account.html')


def test_page(request):
    return render(request, 'dig_marketplace/index.html')