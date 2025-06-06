from django import forms
from .models import Component
from warehouses.models import Warehouse
from suppliers.models import Supplier

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['name', 'part_number', 'category', 'quantity', 'image', 'warehouse', 'supplier']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full rounded-[0.5rem] border-red-300 text-lg shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]',
                'placeholder': 'Введите название компонента'
            }),
            'part_number': forms.TextInput(attrs={
                'class': 'block w-full rounded-[0.5rem] border-red-300 text-lg shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]',
                'placeholder': 'Введите номер части'
            }),
            'category': forms.TextInput(attrs={
                'class': 'block w-full rounded-[0.5rem] border-red-300 text-lg shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]',
                'placeholder': 'Введите категорию'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'block w-full rounded-[0.5rem] border-red-300 text-lg shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]',
                'placeholder': 'Введите количество',
                'min': '0'
            }),
            'image': forms.FileInput(attrs={
                'class': 'block w-full rounded-[0.5rem] border-red-300 text-lg shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]'
            }),
            'warehouse': forms.Select(attrs={
                'class': 'block w-full rounded-[0.5rem] border-red-300 text-lg shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]'
            }),
            'supplier': forms.Select(attrs={
                'class': 'block w-full rounded-[0.5rem] border-red-300 text-lg shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Убедимся, что выпадающие списки заполнены данными из соответствующих моделей
        if 'warehouse' in self.fields:
            self.fields['warehouse'].queryset = Warehouse.objects.all()
        if 'supplier' in self.fields:
            self.fields['supplier'].queryset = Supplier.objects.all()

# Примечание: Убедитесь, что модели Warehouse и Supplier определены в models.py