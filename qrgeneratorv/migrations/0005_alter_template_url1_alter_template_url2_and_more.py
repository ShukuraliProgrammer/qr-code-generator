# Generated by Django 4.0.6 on 2022-07-29 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrgeneratorv', '0004_remove_qrcode_tariff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='url1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='template',
            name='url2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='template',
            name='url3',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ссылка'),
        ),
    ]
