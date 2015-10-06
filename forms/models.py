from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=128)
    file = models.FileField(upload_to='forms')

    def __unicode__(self):
        return self.name
