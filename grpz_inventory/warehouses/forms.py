from django import forms
from .models import Warehouse

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name', 'location', 'capacity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full rounded-[0.5rem] border-gray-300 shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]'}),
            'location': forms.TextInput(attrs={'class': 'block w-full rounded-[0.5rem] border-gray-300 shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]'}),
            'capacity': forms.NumberInput(attrs={'class': 'block w-full rounded-[0.5rem] border-gray-300 shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]'}),
        }