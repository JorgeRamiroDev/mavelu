# Generated by Django 4.2.6 on 2023-11-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("produto", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="categorie",
            name="imagem",
            field=models.ImageField(default=1, upload_to="foto_categorie/"),
            preserve_default=False,
        ),
    ]
