# Generated by Django 4.1 on 2023-06-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0008_etiqueta'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='esCentroFormacion',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='institucion',
            name='esCuidados',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='institucion',
            name='esEducativa',
            field=models.BooleanField(default=False),
        ),
    ]
