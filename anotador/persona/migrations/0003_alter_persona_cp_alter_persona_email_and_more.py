# Generated by Django 4.1 on 2023-04-19 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0008_etiqueta'),
        ('persona', '0002_auto_20220426_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='cp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nacionalidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros.nacionalidad'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='piso_dpto',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
