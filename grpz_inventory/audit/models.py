from django.db import models

class AuditLog(models.Model):
    
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, verbose_name='Пользователь')
    action = models.CharField(max_length=255, verbose_name='Действие')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время')
    details = models.TextField(blank=True, verbose_name='Подробности')
    old_value = models.TextField(blank=True, verbose_name='Старое значение')
    new_value = models.TextField(blank=True, verbose_name='Новое значение')

    class Meta:
        verbose_name = 'Лог аудита'
        verbose_name_plural = 'Логи аудита'

    def __str__(self):
        return f"{self.user} - {self.action} - {self.timestamp}"