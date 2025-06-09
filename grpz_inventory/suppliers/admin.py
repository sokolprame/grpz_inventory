# suppliers/admin.py
from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'terms')
    search_fields = ('name', 'contact_info')
