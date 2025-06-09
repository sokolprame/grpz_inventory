from django.contrib import admin
from .models import Component

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'part_number',
        'category',
        'description',
        'unit',
        'barcode',
        'quantity',
        'warehouse',
        'supplier',
        'created_at',
        'updated_at',
        'image',
    )
    list_filter = ('warehouse', 'supplier', 'category', 'unit', 'created_at', 'updated_at')
    search_fields = ('name', 'part_number', 'category', 'description', 'barcode')
