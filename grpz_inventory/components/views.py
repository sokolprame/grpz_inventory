from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Component
from .forms import ComponentForm

def is_clerk(user):
    return user.is_authenticated and user.role in ['warehouse_worker', 'admin']

def component_list(request):
    try:
        components = Component.objects.all()
        can_edit_component = request.user.is_authenticated and request.user.role in ['admin', 'warehouse_worker']
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
        return render(request, 'components/list.html', {
            'components': components,
            'can_edit_component': can_edit_component
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def component_detail(request, pk):
    component = get_object_or_404(Component, pk=pk)
    can_edit_component = request.user.is_authenticated and request.user.role in ['admin', 'warehouse_worker']
    return render(request, 'components/detail.html', {
        'component': component,
        'can_edit_component': can_edit_component
    })

@login_required
@user_passes_test(is_clerk)
def add_component(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST, request.FILES)
        if form.is_valid():
            component = form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'pk': component.pk,
                    'name': component.name,
                    'quantity': component.quantity,
                    'image': component.image.url if component.image else None,
                    'message': 'Компонент добавлен!'
                }, status=201)
            return redirect('components:component_list')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors.as_json()  # Используем as_json() для структурированного вывода ошибок
                }, status=400)
            return render(request, 'components/add.html', {'form': form})
    form = ComponentForm()
    return render(request, 'components/add.html', {'form': form})

@login_required
@user_passes_test(is_clerk)
def edit_component(request, pk):
    component = get_object_or_404(Component, pk=pk)
    if request.method == 'POST':
        form = ComponentForm(request.POST, request.FILES, instance=component)
        if form.is_valid():
            component = form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'pk': component.pk,
                    'name': component.name,
                    'quantity': component.quantity,
                    'image': component.image.url if component.image else None,
                    'message': 'Компонент обновлён!'
                }, status=200)
            return redirect('components:component_list')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': form.errors.as_json()  # Используем as_json() для структурированного вывода ошибок
                }, status=400)
            return render(request, 'components/add.html', {'form': form, 'component': component})
    form = ComponentForm(instance=component)
    return render(request, 'components/add.html', {'form': form, 'component': component})

@login_required
@user_passes_test(is_clerk)
def delete_component(request, pk):
    component = get_object_or_404(Component, pk=pk)
    if request.method == 'DELETE':
        component.delete()
        return JsonResponse({'success': True, 'message': 'Компонент удалён!'}, status=200)
    return JsonResponse({'success': False, 'error': 'Метод не поддерживается'}, status=405)