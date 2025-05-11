from django.shortcuts import render, get_object_or_404
from .models import Component

def component_list(request):
    components = Component.objects.all()
    return render(request, 'components/list.html', {'components': components})

def component_detail(request, pk):
    component = get_object_or_404(Component, pk=pk)
    return render(request, 'components/detail.html', {'component': component})