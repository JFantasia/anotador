# Generated by Django 4.1 on 2022-09-05 06:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("parametros", "0007_institucion"),
        ("salud", "0013_auto_20220504_2259"),
    ]

    operations = [
        migrations.AddField(
            model_name="intervencion",
            name="institucion",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stin",
                to="parametros.institucion",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="agendaturnos",
            name="hora_desde",
            field=models.TimeField(default=datetime.time(3, 6, 58, 729327)),
        ),
        migrations.AlterField(
            model_name="agendaturnos",
            name="hora_hasta",
            field=models.TimeField(default=datetime.time(3, 6, 58, 729352)),
        ),
        migrations.AlterField(
            model_name="ficha",
            name="genero",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sfg",
                to="parametros.genero",
            ),
        ),
    ]