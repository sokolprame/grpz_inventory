# Generated by Django 5.2 on 2025-05-03 08:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('components', '0002_initial'),
        ('orders', '0001_initial'),
        ('suppliers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создал'),
        ),
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppliers.supplier', verbose_name='Поставщик'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='component',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='components.component', verbose_name='Комплектующее'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ'),
        ),
    ]
