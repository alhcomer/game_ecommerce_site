# Generated by Django 4.1.1 on 2022-11-09 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gaming_shop", "0002_alter_product_platforms_alter_product_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(default="images/default.png", upload_to="images/"),
        ),
    ]
