# Generated by Django 4.1.1 on 2022-09-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Formulario",
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
                ("nome", models.CharField(max_length=255)),
                ("cepdestino", models.CharField(max_length=9)),
                ("ceporigem", models.CharField(max_length=9)),
                ("qtd", models.IntegerField()),
                ("telefone", models.CharField(max_length=11)),
            ],
        ),
    ]