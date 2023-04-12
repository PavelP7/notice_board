from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from django.urls import reverse

class Notice(models.Model):

    TANKS = 'TN'
    HEALERS = 'HL'
    DAMAGE_DEALERS = 'DD'
    VENDORS = 'VD'
    GUILD_MASTERS = 'GM'
    QUESTY_GIVERS = 'QG'
    BLACKSMITHS = 'BS'
    LEATHERWORKERS = 'LW'
    POTIONEERS = 'PT'
    MASTERS_OF_SPELLS = 'MS'

    NAMES = [
        (TANKS, 'Танки'),
        (HEALERS, 'Хилы'),
        (DAMAGE_DEALERS, 'ДД'),
        (VENDORS, 'Торговцы'),
        (GUILD_MASTERS, 'Гилдмастеры'),
        (QUESTY_GIVERS, 'Квестигиверы'),
        (BLACKSMITHS, 'Кузнецы'),
        (LEATHERWORKERS, 'Кожевники'),
        (POTIONEERS, 'Зельевары'),
        (MASTERS_OF_SPELLS, 'Мастера заклинаний'),
    ]

    title = models.TextField()
    category = models.CharField(max_length=2, choices=NAMES, default=VENDORS)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    content = tinymce_models.HTMLField()

    def __str__(self):
        return f'{self.author} {self.title[:20]}'

    def get_absolute_url(self):
        return reverse('notice_create')

class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} {self.text[:20]}'
