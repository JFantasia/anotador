# Generated by Django 4.1 on 2023-06-06 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0024_alter_agendaturnos_hora_desde_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendaturnos',
            name='hora_desde',
            field=models.TimeField(default=datetime.time(6, 59, 48, 342934)),
        ),
        migrations.AlterField(
            model_name='agendaturnos',
            name='hora_hasta',
            field=models.TimeField(default=datetime.time(6, 59, 48, 342944)),
        ),
    ]
