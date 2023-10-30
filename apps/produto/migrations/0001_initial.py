# Generated by Django 4.2.6 on 2023-10-29 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ItemOrder",
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
                ("nome_produto", models.CharField(max_length=100)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantidade", models.PositiveIntegerField()),
                ("descricao", models.TextField()),
            ],
        ),
    ]
