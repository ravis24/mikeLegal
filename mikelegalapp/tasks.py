# campaigns/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import Subscriber, Campaign
from mikeLegal.celery import app
from mikeLegal import settings
import datetime

@shared_task
def send_daily_campaigns():

    active_subscribers = Subscriber.objects.filter(is_active=True)
    
    daily_campaign = Campaign.objects.filter(published_date=datetime.date.today()).first()
    
    if not daily_campaign:
        return
    
    subject = daily_campaign.subject
    message = daily_campaign.plain_text_content
    from_email = settings.EMAIL_HOST_USER

    for subscriber in active_subscribers:
        send_mail(subject, message, from_email, [subscriber.email], fail_silently=False)
    return "Sent"
