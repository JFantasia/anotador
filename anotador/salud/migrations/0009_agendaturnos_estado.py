# Generated by Django 3.2 on 2022-05-01 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0008_auto_20220501_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendaturnos',
            name='estado',
            field=models.CharField(choices=[('P', 'Pendiente'), ('F', 'Finalizada'), ('C', 'Cancelada')], default='P', max_length=1, verbose_name='Estado'),
        ),
    ]
