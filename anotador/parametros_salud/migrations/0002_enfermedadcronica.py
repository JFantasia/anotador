# Generated by Django 3.2 on 2022-05-01 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametros_salud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnfermedadCronica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Enfermedades Crónicas',
            },
        ),
    ]
