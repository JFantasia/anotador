# Generated by Django 4.1 on 2023-08-09 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0030_alter_agendaturnos_hora_desde_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendaturnos',
            name='hora_desde',
            field=models.TimeField(default=datetime.time(5, 24, 53, 123792)),
        ),
        migrations.AlterField(
            model_name='agendaturnos',
            name='hora_hasta',
            field=models.TimeField(default=datetime.time(5, 24, 53, 123805)),
        ),
    ]
