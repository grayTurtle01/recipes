# Generated by Django 3.2.8 on 2021-12-17 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]