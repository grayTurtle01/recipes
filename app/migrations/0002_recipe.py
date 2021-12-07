# Generated by Django 3.2.8 on 2021-12-06 18:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=30)),
                ('ingridients', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=400)),
                ('tags', models.CharField(max_length=50)),
                ('descripion', models.CharField(max_length=400)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]