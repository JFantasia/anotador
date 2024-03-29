# Generated by Django 3.2 on 2022-05-01 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parametros_trabajo', '0001_initial'),
        ('trabajo', '0004_auto_20220501_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programa',
            name='dependencia',
        ),
        migrations.RemoveField(
            model_name='unidadproductiva',
            name='localidad',
        ),
        migrations.AlterField(
            model_name='ficha',
            name='actividad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros_trabajo.actividad'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros_trabajo.programa'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='trabajo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros_trabajo.trabajo'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='unidad_productiva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametros_trabajo.unidadproductiva'),
        ),
        migrations.AlterField(
            model_name='lista_espera',
            name='actividad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ale', to='parametros_trabajo.actividad'),
        ),
        migrations.DeleteModel(
            name='Actividad',
        ),
        migrations.DeleteModel(
            name='Dependencia',
        ),
        migrations.DeleteModel(
            name='Programa',
        ),
        migrations.DeleteModel(
            name='Rama',
        ),
        migrations.DeleteModel(
            name='Trabajo',
        ),
        migrations.DeleteModel(
            name='UnidadProductiva',
        ),
    ]
