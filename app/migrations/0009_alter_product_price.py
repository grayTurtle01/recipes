# Generated by Django 3.2.8 on 2021-12-18 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
