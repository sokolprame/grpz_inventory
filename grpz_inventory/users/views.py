from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from orders.models import Order 

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматический вход после регистрации
            messages.success(request, 'Регистрация успешна!')
            return redirect('home')  # Перенаправление на главную страницу
        else:
            messages.error(request, 'Ошибка регистрации. Проверьте данные.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/registration/register.html', {'form': form})

def profile(request):
    return render(request, 'users/profile.html')