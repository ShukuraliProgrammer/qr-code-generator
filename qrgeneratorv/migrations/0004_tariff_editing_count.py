# Generated by Django 4.0.6 on 2022-08-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrgeneratorv', '0003_alter_tariff_scan_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariff',
            name='editing_count',
            field=models.IntegerField(default=0, verbose_name='Количество редактирований'),
        ),
    ]
