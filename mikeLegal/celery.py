# email_campaign_manager/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mikeLegal.settings')

app = Celery('mikeLegal')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery beat schedule
app.conf.beat_schedule = {
	'send-mail-every-day' : {
		 'task' : 'mikelegalapp.tasks.send_daily_campaigns',
		 'schedule' : crontab(hour=11,minute=47) 
	}	
}
app.autodiscover_tasks()
