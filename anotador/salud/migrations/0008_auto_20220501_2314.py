# Generated by Django 3.2 on 2022-05-01 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametros_salud', '0002_enfermedadcronica'),
        ('salud', '0007_auto_20220501_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendaturnos',
            name='detalle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='altura',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='autopercepcion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros_salud.autopercepcion'),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='identifica_colores',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros_salud.identificacolores'),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='identifica_letras',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros_salud.venumerosletras'),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='peso',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='presion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros_salud.presionarterial'),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='test_cerca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros_salud.testvistacerca'),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='test_lejos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros_salud.testvistalejos'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='cobertura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametros_salud.cobertura'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='dificultades',
            field=models.ManyToManyField(blank=True, null=True, related_name='dif', to='parametros_salud.Dificultad'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='enfermedades',
            field=models.ManyToManyField(blank=True, null=True, related_name='enf', to='parametros_salud.Enfermedad'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='enfermedades_cronicas',
            field=models.ManyToManyField(blank=True, null=True, related_name='enf_cronicas', to='parametros_salud.EnfermedadCronica'),
        ),
        migrations.AlterField(
            model_name='lista_medicamentos',
            name='detalle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='atencion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='salud.atencion'),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='detalle',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='turnos',
            name='sobreturno',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
