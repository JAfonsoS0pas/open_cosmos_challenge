from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'open_cosmos.settings')

# Create a Celery instance and configure it using the settings from Django.
app = Celery('open_cosmos')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps.
app.autodiscover_tasks()

# Use Redis as the Celery Beat result backend
app.conf.beat_schedule = {
    'update-scheduled-scans': {
        'task': 'business.tasks.consumer',
        'schedule': crontab(),  # Run every minute
    },
}