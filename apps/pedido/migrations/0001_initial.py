# Generated by Django 4.2.6 on 2023-10-29 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("produto", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("data_pedido", models.DateTimeField(auto_now_add=True)),
                ("data_envio", models.DateTimeField(blank=True, null=True)),
                ("data_entrega", models.DateTimeField(blank=True, null=True)),
                (
                    "cliente",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("itens", models.ManyToManyField(to="produto.itemorder")),
            ],
        ),
    ]
