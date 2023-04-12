from .models import Notice, User
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from NoticeBoard.settings import *
from sign.models import Preuser

def periodic_mails():
    last_week = datetime.now() - timedelta(weeks=1)
    notices = Notice.objects.filter(datetime_created__gte=last_week)

    for user in User.objects.all():
        html_content = render_to_string(
            'email_news.html',
            {
                'username': user.username,
                'notices': notices,
            }
        )

        msg = EmailMultiAlternatives(
            subject=EMAIL_SUBJECT,
            to=[f'{user.email}'],
        )

        msg.attach_alternative(html_content, "text/html")
        msg.send()

def periodic_clean_codes():
    last_minute = datetime.now() - timedelta(minutes=1)
    Preuser.objects.filter(datetime_created__lte=last_minute).delete()
