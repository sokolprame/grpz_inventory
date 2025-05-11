from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Warehouse
from .forms import WarehouseForm

def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'warehouses/warehouse_list.html', {'warehouses': warehouses})

def warehouse_create(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Склад успешно добавлен!')
            return redirect('warehouses:warehouse_list')
        else:
            messages.error(request, 'Ошибка при добавлении склада. Проверьте данные.')
    else:
        form = WarehouseForm()
    return render(request, 'warehouses/warehouse_form.html', {'form': form, 'action': 'Добавить'})

def warehouse_edit(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            messages.success(request, 'Склад успешно обновлён!')
            return redirect('warehouses:warehouse_list')
        else:
            messages.error(request, 'Ошибка при обновлении склада. Проверьте данные.')
    else:
        form = WarehouseForm(instance=warehouse)
    return render(request, 'warehouses/warehouse_form.html', {'form': form, 'action': 'Редактировать'})