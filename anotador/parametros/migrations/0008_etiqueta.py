# Generated by Django 4.1 on 2022-10-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0007_institucion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Etiquetas',
            },
        ),
    ]
