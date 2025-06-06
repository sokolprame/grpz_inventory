from django import forms
from .models import Component
from warehouses.models import Warehouse
from suppliers.models import Supplier
from PIL import Image
import os

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
                'class': 'block w-full rounded-[0.5rem] border-red-300 text-lg shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]',
                'accept': 'image/*'  # Ограничиваем выбор только изображениями
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
        if 'warehouse' in self.fields:
            self.fields['warehouse'].queryset = Warehouse.objects.all()
        if 'supplier' in self.fields:
            self.fields['supplier'].queryset = Supplier.objects.all()

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Проверка размера файла (не больше 5MB)
            if image.size > 5 * 1024 * 1024:  # 5MB
                raise forms.ValidationError('Изображение слишком большое. Максимальный размер: 5MB.')
            
            # Проверка формата файла
            if not image.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                raise forms.ValidationError('Поддерживаются только форматы PNG, JPG, JPEG и GIF.')

            # Сжатие изображения
            img = Image.open(image)
            if img.size[0] > 1200 or img.size[1] > 1200:  # Если ширина или высота больше 1200px
                img.thumbnail((1200, 1200))
                image.file.seek(0)
                img.save(image.file, format=img.format, quality=85)
                image.file.truncate()
        return image