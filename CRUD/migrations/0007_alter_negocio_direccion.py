# Generated by Django 5.1.6 on 2025-04-04 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0006_alter_like_unique_together_remove_like_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negocio',
            name='direccion',
            field=models.CharField(blank=True, max_length=455),
        ),
    ]
