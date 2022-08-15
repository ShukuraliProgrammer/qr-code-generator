from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qrcored.settings')

app = Celery('config')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Tashkent')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'send-email-every-day-at-8': {
        'task': 'qrgeneratorv.tasks.send_beat_email',
        'schedule': crontab(minute=15, hour=6, day_of_week="monday", day_of_month="1-7", month_of_year="8"),
        # 'args': ()
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')