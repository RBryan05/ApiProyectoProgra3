# Generated by Django 5.1.6 on 2025-05-03 04:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0018_respuesta_usuario_alter_respuesta_negocio'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRUD.producto'),
        ),
    ]
