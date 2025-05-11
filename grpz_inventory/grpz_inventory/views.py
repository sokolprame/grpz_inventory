from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

from components.models import Component
from warehouses.models import Warehouse

User = get_user_model()

def home(request):
    total_components  = Component.objects.count()
    warehouse_count   = Warehouse.objects.count()
    user_count        = User.objects.count()
    low_stock_count   = Component.objects.filter(quantity__lt=10).count()
    recent_components = Component.objects.order_by('-created_at')[:5]

    return render(request, 'home.html', {
        'total_components': total_components,
        'warehouse_count': warehouse_count,
        'user_count': user_count,
        'low_stock_count': low_stock_count,
        'recent_components': recent_components,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна! Добро пожаловать!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка при регистрации. Проверьте данные.')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы.')
    return redirect('login')

def profile(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Пожалуйста, войдите в систему.')
        return redirect('login')
    return render(request, 'users/profile.html', {'user': request.user})
