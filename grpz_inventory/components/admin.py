from django.contrib import admin
from .models import Component

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'part_number', 'quantity', 'warehouse')
    list_filter = ('warehouse', 'supplier')
    search_fields = ('name', 'part_number')