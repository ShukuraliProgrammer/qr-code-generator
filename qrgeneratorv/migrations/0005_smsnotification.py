# Generated by Django 4.0.6 on 2022-08-09 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qrgeneratorv', '0004_tariff_admin_panel_tariff_sms_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allscans', models.CharField(max_length=100, verbose_name='Все отсканированные коды')),
                ('os_enter_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='ОС Enter Counts')),
                ('mobile_enter_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='Мобильный Enter Counts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sms_notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'СМС оповещение',
                'verbose_name_plural': 'СМС оповещения',
            },
        ),
    ]
