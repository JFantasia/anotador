# Generated by Django 4.1 on 2022-09-05 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("parametros", "0007_institucion"),
        ("persona", "0002_auto_20220426_2304"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ficha",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("situacion_violencia", models.BooleanField(default=False)),
                ("situacion_habitacional", models.BooleanField(default=False)),
                ("situacion_familiar", models.BooleanField(default=False)),
                ("situacion_justicia", models.BooleanField(default=False)),
                ("situacion_salud", models.BooleanField(default=False)),
                ("situacion_consumo", models.BooleanField(default=False)),
                (
                    "genero",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="parametros.genero",
                    ),
                ),
                (
                    "persona",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gfp",
                        to="persona.persona",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Fichas",},
        ),
        migrations.CreateModel(
            name="Intervencion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField()),
                ("detalle", models.TextField()),
                (
                    "institucion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gtin",
                        to="parametros.institucion",
                    ),
                ),
                (
                    "persona",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="generos.ficha"
                    ),
                ),
                (
                    "tipo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gti",
                        to="parametros.tipointervecion",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Intervenciones",},
        ),
    ]