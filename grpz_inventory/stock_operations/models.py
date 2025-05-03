from django.db import models

class StockOperation(models.Model):
    
    OPERATION_TYPES = [
        ('in', 'Поступление'),
        ('out', 'Выдача'),
    ]
    operation_type = models.CharField(max_length=3, choices=OPERATION_TYPES, verbose_name='Тип операции')
    component = models.ForeignKey('components.Component', on_delete=models.CASCADE, verbose_name='Комплектующее')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    warehouse = models.ForeignKey('warehouses.Warehouse', on_delete=models.CASCADE, verbose_name='Склад')
    operation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата операции')
    performed_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, verbose_name='Исполнитель')

    class Meta:
        verbose_name = 'Складская операция'
        verbose_name_plural = 'Складские операции'

    def __str__(self):
        return f"{self.operation_type} {self.component} ({self.quantity})"

class OperationItem(models.Model):

    operation = models.ForeignKey(StockOperation, on_delete=models.CASCADE, verbose_name='Операция')
    component = models.ForeignKey('components.Component', on_delete=models.CASCADE, verbose_name='Комплектующее')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Элемент операции'
        verbose_name_plural = 'Элементы операции'

    def __str__(self):
        return f"{self.component} ({self.quantity})"

