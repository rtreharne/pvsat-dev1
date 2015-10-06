from django.db import models
from sorl.thumbnail import ImageField

class Speaker(models.Model):
    forename = models.CharField(max_length=128, unique = True)
    surname = models.CharField(max_length=128, unique = True)
    affiliation = models.CharField(max_length=128)
    title = models.CharField(max_length=128, blank=True)
    pic = ImageField(upload_to='logo_images', blank=True)
    url = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __unicode__(self):
        return self.surname

class Theme(models.Model):
    title = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.title
