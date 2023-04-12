from django.db.models.signals import post_save
from .models import Preuser
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from NoticeBoard.settings import *

def send_confirmation(user_id):
    user = Preuser.objects.get(pk=user_id)

    html_content = render_to_string(
        'sign/email_signup_confirmation.html',
        {
            'username': user.username,
            'code': user.code,
        }
    )

    msg = EmailMultiAlternatives(
        subject=EMAIL_SUBJECT,
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=[f'{user.email}'],
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()

@receiver(post_save, sender=Preuser)
def notify_confirmation(sender, instance, **kwargs):
    send_confirmation(instance.pk)
