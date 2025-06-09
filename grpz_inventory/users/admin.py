﻿from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'role',
    )
    list_filter = ('role',)
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Дополнительные поля', {
            'fields': ('role',),
        }),
    )
