# Generated by Django 4.2.6 on 2023-11-11 01:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("produto", "0003_remove_categorie_produtos_itemorder_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="itemorder",
            name="imagem",
            field=models.ImageField(default=1, upload_to="foto_perfil/"),
            preserve_default=False,
        ),
    ]
