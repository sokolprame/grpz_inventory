# audit/admin.py
from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp', 'short_details')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username', 'action', 'details', 'old_value', 'new_value')
    readonly_fields = ('user', 'action', 'timestamp', 'details', 'old_value', 'new_value')

    def short_details(self, obj):
        return (obj.details[:50] + '...') if obj.details and len(obj.details) > 50 else obj.details
    short_details.short_description = 'Подробности'
