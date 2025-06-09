# orders/admin.py
from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier', 'order_date', 'status', 'created_by')
    list_filter = ('status', 'supplier')
    search_fields = ('supplier__name', 'created_by__username')
    date_hierarchy = 'order_date'
    ordering = ('-order_date',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'component', 'quantity')
    list_filter = ('component',)
    search_fields = ('component__name', 'order__id')
