# Generated by Django 3.2 on 2022-05-02 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0009_agendaturnos_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendaturnos',
            name='hora_desde',
            field=models.TimeField(default=datetime.time(6, 49, 56, 684551)),
        ),
        migrations.AddField(
            model_name='agendaturnos',
            name='hora_hasta',
            field=models.TimeField(default=datetime.time(6, 49, 56, 684585)),
        ),
    ]