from django.db.models.signals import post_save
from .models import Reaction
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from NoticeBoard.settings import *

def send_accepted_reaction(reaction_id):
    reaction = Reaction.objects.get(pk=reaction_id)

    html_content = render_to_string(
        'email_accepted_reaction.html',
        {
            'username': reaction.user.username,
            'text': reaction.text[:20] + '...',
            'datetime_created': reaction.datetime_created,
        }
    )

    msg = EmailMultiAlternatives(
        subject=EMAIL_SUBJECT,
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=[f'{reaction.user.email}'],
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_created_reaction(reaction_id):
    reaction = Reaction.objects.select_related('notice').get(pk=reaction_id)
    notice = reaction.notice

    html_content = render_to_string(
        'email_created_reaction.html',
        {
            'username': notice.author.username,
            'title': notice.title,
            'link': f'{SITE_URL}/board/{notice.id}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=EMAIL_SUBJECT,
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=[f'{notice.author.email}'],
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()

@receiver(post_save, sender=Reaction)
def notify_created_reaction(sender, instance, **kwargs):
    send_created_reaction(instance.pk)
