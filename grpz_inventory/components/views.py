from django.shortcuts import render, get_object_or_404
from .models import Component

def component_list(request):
    components = Component.objects.all()
    return render(request, 'components/list.html', {'components': components})

def component_detail(request, pk):
    component = get_object_or_404(Component, pk=pk)
    return render(request, 'components/detail.html', {'component': component})

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
                'image': component.image.url if component.image else None
            })
        return JsonResponse({'success': False, 'error': form.errors.as_text()})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})