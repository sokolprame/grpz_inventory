from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    contact_info = models.TextField(blank=True, verbose_name='Контактные данные')
    terms = models.TextField(blank=True, verbose_name='Условия поставки')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name
