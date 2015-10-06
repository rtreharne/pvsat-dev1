from django.db import models
from sorl.thumbnail import ImageField

class Member(models.Model):
    forename = models.CharField(max_length=128, unique = True)
    surname = models.CharField(max_length=128, unique = True)
    affiliation = models.CharField(max_length=128)
    role = models.CharField(max_length=128, blank=True)
    url = models.URLField()
    pic = ImageField(upload_to='committee_img', blank=True)

    def __unicode__(self):
        return self.surname
