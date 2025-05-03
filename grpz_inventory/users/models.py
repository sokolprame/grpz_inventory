from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('manager', 'Менеджер'),
        ('engineer', 'Инженер'),
        ('warehouse_worker', 'Кладовщик'),
        ('custom', 'Кастомная роль'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='manager', verbose_name='Роль')
    telegram_id = models.CharField(max_length=50, blank=True, null=True, unique=True, verbose_name='Telegram ID')
    is_2fa_enabled = models.BooleanField(default=False, verbose_name='Включена двухфакторная аутентификация')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username