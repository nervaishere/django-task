from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_interview.settings')

app = Celery('backend_interview')
app.conf.enable_utc = False

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


app.conf.beat_schedule = {
    'add-every-day': {
        'task': 'user_management.tasks.send_sms',
        'schedule': crontab(hour=23, minute=59),
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'