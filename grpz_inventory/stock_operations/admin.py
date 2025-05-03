# stock_operations/admin.py
from django.contrib import admin
from .models import StockOperation, OperationItem

admin.site.register(StockOperation)
admin.site.register(OperationItem)