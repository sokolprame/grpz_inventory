from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from components.models import Component

def home(request):
    total_components = Component.objects.count()
    low_stock_components = Component.objects.filter(quantity__lt=10).count()
    recent_components = Component.objects.order_by('-created_at')[:5]
    context = {
        'total_components': total_components,
        'low_stock_components': low_stock_components,
        'recent_components': recent_components,
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка при регистрации. Проверьте данные.')
    else:
        form = UserCreationForm()
    return render(request, 'users/registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли!')
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    else:
        form = AuthenticationForm()
    return render(request, 'users/registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли.')
    return redirect('home')

def profile(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Войдите, чтобы просмотреть профиль.')
        return redirect('login')
    return render(request, 'users/profile.html')