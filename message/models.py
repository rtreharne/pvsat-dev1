from django.db import models
from django.utils import timezone
from time import time

class Message(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    message = models.TextField(max_length=5000)
    date = models.DateTimeField(default=timezone.datetime.today())

    def __unicode__(self):
        return self.subject

