import os

from celery import Celery
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')

app = Celery('app_score')

app.conf.beat_schedule = {
    'cada_1_minuto_cs': {
        'task': 'app_stats.tasks.stats_user_cs',
        'schedule': crontab(),
        'args': ()
    },
    'cada_1_minuto_lol': {
        'task': 'app_stats.tasks.stats_user_lol',
        'schedule': crontab(),
        'args': ()
    },
}


app.conf.timezone = 'UTC'

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')