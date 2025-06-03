from django import forms
from .models import Component

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['name', 'quantity', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full rounded-[0.5rem] border-red-300 text-lg shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]'}),
            'quantity': forms.NumberInput(attrs={'class': 'block w-full rounded-[0.5rem] border-red-300 text-lg shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]'}),
            'image': forms.FileInput(attrs={'class': 'block w-full rounded-[0.5rem] border-red-300 text-lg shadow-sm focus:border-[#dc2626] focus:ring-[#dc2626]'}),
        }