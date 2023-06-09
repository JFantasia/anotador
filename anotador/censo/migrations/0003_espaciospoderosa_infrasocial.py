# Generated by Django 4.1 on 2023-06-08 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('censo', '0002_materialespared_materialespiso_materialestecho_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EspaciosPoderosa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Espacios de la Poderosa',
            },
        ),
        migrations.CreateModel(
            name='InfraSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centrosSalud', models.BooleanField()),
                ('atencionPostaSalud', models.BooleanField()),
                ('turnosPostaSalud', models.BooleanField()),
                ('frecuenciaAtencionSalud', models.CharField(blank=True, choices=[('1S', '1 vez a la semana'), ('2S', '2 veces a la semana'), ('+2S', 'Más de 2 veces a la semana'), ('1M', '1 vez al mes'), ('1A', '1 vez al año'), ('CM', 'Circunstancialmente')], default='1', max_length=3, null=True, verbose_name='Frecuencia de asistencia a Centros de Salud')),
                ('experienciaAtencion', models.TextField(blank=True, null=True)),
                ('problemasCronicosFamiliares', models.BooleanField()),
                ('lugaresAtencion', models.TextField(blank=True, null=True)),
                ('ambulanciaIngresa', models.BooleanField()),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='censo.encuesta')),
                ('espaciosPoderosa', models.ManyToManyField(related_name='infraEspacios', to='censo.espaciospoderosa', verbose_name='A que espacios de LP asiste')),
            ],
            options={
                'verbose_name_plural': '6-Infraestructura Social',
            },
        ),
    ]
