from django.db import models

class Component(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    part_number = models.CharField(max_length=50, unique=True, verbose_name='Артикул')
    category = models.CharField(max_length=100, blank=True, verbose_name='Категория')
    description = models.TextField(blank=True, verbose_name='Описание')
    unit = models.CharField(max_length=20, default='шт', verbose_name='Единица измерения')
    barcode = models.CharField(max_length=100, unique=True, blank=True, null=True, verbose_name='Штрих-код')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    warehouse = models.ForeignKey('warehouses.Warehouse', on_delete=models.CASCADE, verbose_name='Склад')
    supplier = models.ForeignKey('suppliers.Supplier', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Поставщик')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to='components/', blank=True, null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Комплектующее'
        verbose_name_plural = 'Комплектующие'

    def __str__(self):
        return f"{self.name} ({self.part_number})"