# warehouses/admin.py
from django.contrib import admin
from .models import Warehouse

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'responsible', 'capacity', 'location')
    list_filter = ('responsible',)
    search_fields = ('name', 'address', 'location')
