from django.db import models

class Preuser(models.Model):
    code = models.CharField(max_length=4, unique=True)
    username = models.TextField()
    email = models.TextField()
    password = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
