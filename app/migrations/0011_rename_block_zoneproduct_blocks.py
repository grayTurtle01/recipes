# Generated by Django 3.2.8 on 2021-12-20 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_zoneproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zoneproduct',
            old_name='block',
            new_name='blocks',
        ),
    ]
