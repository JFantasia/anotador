# Generated by Django 4.1 on 2023-08-09 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0033_alter_agendaturnos_hora_desde_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendaturnos',
            name='hora_desde',
            field=models.TimeField(default=datetime.time(6, 13, 46, 186415)),
        ),
        migrations.AlterField(
            model_name='agendaturnos',
            name='hora_hasta',
            field=models.TimeField(default=datetime.time(6, 13, 46, 186429)),
        ),
    ]
