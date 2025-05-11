from django import forms
from .models import Order, OrderItem
from suppliers.models import Supplier
from components.models import Component

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supplier', 'status']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'w-full border border-red-300 rounded-md px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 text-lg'}),
            'status': forms.Select(attrs={'class': 'w-full border border-red-300 rounded-md px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 text-lg'}),
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['component', 'quantity']
        widgets = {
            'component': forms.Select(attrs={'class': 'w-full border border-red-300 rounded-md px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 text-lg'}),
            'quantity': forms.NumberInput(attrs={'class': 'w-full border border-red-300 rounded-md px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 text-lg', 'min': 1}),
        }