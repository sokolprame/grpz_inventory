from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from orders.models import Order
from components.models import Component
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from django import forms

# Получаем кастомную модель пользователя
User = get_user_model()

# Проверка, является ли пользователь администратором
def is_admin(user):
    return user.is_staff or user.is_superuser

# Форма для редактирования пользователя
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации. Проверьте данные.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/registration/register.html', {'form': form})

@login_required
def profile(request):
    orders = Order.objects.filter(created_by=request.user).prefetch_related('orderitem_set')
    components = Component.objects.filter(orderitem__order__created_by=request.user).distinct()
    print(f"Загружено заказов для {request.user.username}: {orders.count()}")
    print(f"Компоненты пользователя {request.user.username}: {components.count()}")
    return render(request, 'users/profile.html', {'orders': orders, 'components': components})

@login_required
def download_profile_report(request):
    user = request.user
    components = Component.objects.filter(orderitem__order__created_by=user).distinct()
    orders = Order.objects.filter(created_by=user).prefetch_related('orderitem_set')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="profile_report_{user.username}.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    
    try:
        pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
        p.setFont('Arial', 12)
    except Exception as e:
        return HttpResponse(f"Ошибка загрузки шрифта: {str(e)}", status=500)

    p.drawString(100, 800, "Отчёт по профилю пользователя")
    p.drawString(100, 780, f"Пользователь: {user.username}")
    p.drawString(100, 760, f"Email: {user.email if user.email else 'Не указан'}")
    p.drawString(100, 740, f"Дата регистрации: {user.date_joined.strftime('%d.%m.%Y %H:%M')}")

    y = 700
    p.drawString(100, y, "Компоненты:")
    y -= 20
    if components:
        for component in components:
            p.drawString(100, y, f"Название: {component.name}, Количество: {component.quantity}")
            y -= 20
            if y < 100:
                p.showPage()
                p.setFont('Arial', 12)
                y = 800
    else:
        p.drawString(100, y, "Компоненты отсутствуют")
        y -= 20

    y -= 20
    p.drawString(100, y, "Заказы:")
    y -= 20
    if orders:
        for order in orders:
            order_info = f"Заказ #{order.id} от {order.order_date.strftime('%d.%m.%Y %H:%M')} (Поставщик: {order.supplier})"
            p.drawString(100, y, order_info)
            y -= 20
            if y < 100:
                p.showPage()
                p.setFont('Arial', 12)
                y = 800
    else:
        p.drawString(100, y, "Заказы отсутствуют")
        y -= 20

    p.showPage()
    p.save()
    return response

@login_required
@user_passes_test(is_admin)
def user_list(request):
    users = User.objects.all().order_by('username')
    return render(request, 'users/admin/user_list.html', {'users': users})

@login_required
@user_passes_test(is_admin)
def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Пользователь {user.username} успешно обновлён.')
            return redirect('users:user_list')
        else:
            messages.error(request, 'Ошибка при обновлении пользователя.')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'users/admin/user_edit.html', {'form': form, 'user': user})

@login_required
@user_passes_test(is_admin)
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        if user != request.user:
            user.delete()
            messages.success(request, f'Пользователь {user.username} удалён.')
        else:
            messages.error(request, 'Нельзя удалить самого себя.')
        return redirect('users:user_list')
    return render(request, 'users/admin/user_delete.html', {'user': user})