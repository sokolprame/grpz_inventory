from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm, OrderItemForm

def order_create(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        order_item_form = OrderItemForm(request.POST)
        if order_form.is_valid() and order_item_form.is_valid():
            order = order_form.save(commit=False)
            order.created_by = request.user
            order.save()
            order_item = order_item_form.save(commit=False)
            order_item.order = order
            order_item.save()
            messages.success(request, 'Заказ успешно создан!')
            return redirect('users:profile')
        else:
            messages.error(request, 'Ошибка при создании заказа. Проверьте данные.')
    else:
        order_form = OrderForm()
        order_item_form = OrderItemForm()
    return render(request, 'orders/order_form.html', {'order_form': order_form, 'order_item_form': order_item_form})