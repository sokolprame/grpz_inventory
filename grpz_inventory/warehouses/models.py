from django.db import models

class Warehouse(models.Model):
    
    name = models.CharField(max_length=255, verbose_name='Название')
    address = models.TextField(verbose_name='Адрес')
    responsible = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, verbose_name='Ответственный')
    location = models.CharField(max_length=200, blank=True)  # Добавлено поле местоположения
    capacity = models.PositiveIntegerField(default=0)       # Добавлено поле вместимости

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.name
