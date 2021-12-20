# Generated by Django 3.2.8 on 2021-12-20 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_zonemenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZoneMenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.zoneproduct')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.zonemenu')),
            ],
        ),
    ]