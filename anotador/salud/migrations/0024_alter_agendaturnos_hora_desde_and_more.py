# Generated by Django 4.1 on 2023-05-13 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0023_remove_ficha_enfermedades_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendaturnos',
            name='hora_desde',
            field=models.TimeField(default=datetime.time(20, 25, 7, 570453)),
        ),
        migrations.AlterField(
            model_name='agendaturnos',
            name='hora_hasta',
            field=models.TimeField(default=datetime.time(20, 25, 7, 570464)),
        ),
    ]