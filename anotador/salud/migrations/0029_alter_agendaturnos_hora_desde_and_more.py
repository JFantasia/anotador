# Generated by Django 4.1 on 2023-06-26 11:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0028_alter_agendaturnos_hora_desde_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendaturnos',
            name='hora_desde',
            field=models.TimeField(default=datetime.time(8, 5, 30, 593093)),
        ),
        migrations.AlterField(
            model_name='agendaturnos',
            name='hora_hasta',
            field=models.TimeField(default=datetime.time(8, 5, 30, 593103)),
        ),
    ]
