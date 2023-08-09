# Generated by Django 4.1 on 2023-08-09 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametros', '0011_delete_espaciotrabajo'),
        ('persona', '0004_alter_persona_cuit'),
        ('organizacion', '0003_remove_reserva_espacio_reserva_solicitantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Tareas',
            },
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('planificacion', models.DateField()),
                ('limite', models.DateField(blank=True, null=True)),
                ('detalle', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('F', 'Finalizada'), ('C', 'Cancelada')], default='P', max_length=1, verbose_name='Estado')),
                ('organizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacion.organizacion')),
                ('relaciones', models.ManyToManyField(blank=True, null=True, to='parametros.institucion')),
                ('responsable', models.ManyToManyField(to='persona.persona')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacion.tipotarea')),
            ],
            options={
                'verbose_name_plural': 'Tareas',
            },
        ),
    ]