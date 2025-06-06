from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Component
from .forms import ComponentForm

# Список компонентов
def component_list(request):
    try:
        components = Component.objects.all()
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = {
                'components': [
                    {
                        'pk': component.pk,
                        'name': component.name,
                        'part_number': component.part_number,
                        'quantity': component.quantity,
                        'image': component.image.url if component.image else None,
                        'warehouse': component.warehouse.name if component.warehouse else None,
                        'supplier': component.supplier.name if component.supplier else None
                    }
                    for component in components
                ]
            }
            return JsonResponse(data)
        return render(request, 'components/list.html', {'components': components})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Детали компонента
def component_detail(request, pk):
    component = get_object_or_404(Component, pk=pk)
    return render(request, 'components/detail.html', {'component': component})

# Добавление компонента
@login_required

def add_component(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST, request.FILES)
        if form.is_valid():
            component = form.save()
            return JsonResponse({
                'success': True,
                'pk': component.pk,
                'name': component.name,
                'quantity': component.quantity,
                'image': component.image.url if component.image else None,
                'message': 'Компонент добавлен!'
            })
        return JsonResponse({'success': False, 'error': form.errors.as_text()}, status=400)
    else:
        form = ComponentForm()
    return render(request, 'components/add.html', {'form': form})

# Редактирование компонента
@login_required
def edit_component(request, pk):
    component = get_object_or_404(Component, pk=pk)
    if request.method == 'POST':
        form = ComponentForm(request.POST, request.FILES, instance=component)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True,
                'pk': component.pk,
                'name': component.name,
                'quantity': component.quantity,
                'image': component.image.url if component.image else None,
                'message': 'Компонент обновлён!'
            })
        return JsonResponse({'success': False, 'error': form.errors.as_text()}, status=400)
    else:
        form = ComponentForm(instance=component)
    return render(request, 'components/add.html', {'form': form, 'component': component})

# Удаление компонента
@login_required
def delete_component(request, pk):
    component = get_object_or_404(Component, pk=pk)
    if request.method == 'DELETE':
        component.delete()
        return JsonResponse({'success': True, 'message': 'Компонент удалён!'})
    return JsonResponse({'success': False, 'error': 'Метод не поддерживается'}, status=405)