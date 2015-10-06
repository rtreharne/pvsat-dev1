from django.db import models

class Sponsor(models.Model):
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    logo = models.ImageField(upload_to='logo_images', blank=True)

    def __unicode__(self):
        return self.name
