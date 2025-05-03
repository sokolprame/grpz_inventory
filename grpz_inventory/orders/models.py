from django.db import models

class Order(models.Model):
    
    supplier = models.ForeignKey('suppliers.Supplier', on_delete=models.CASCADE, verbose_name='Поставщик')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'В ожидании'), ('completed', 'Завершено'), ('cancelled', 'Отменено')],
        default='pending',
        verbose_name='Статус'
    )
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, verbose_name='Создал')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказ {self.id} от {self.supplier}"

class OrderItem(models.Model):
   
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    component = models.ForeignKey('components.Component', on_delete=models.CASCADE, verbose_name='Комплектующее')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    class Meta:
        verbose_name = 'Элемент заказа'
        verbose_name_plural = 'Элементы заказа'

    def __str__(self):
        return f"{self.component} ({self.quantity})"