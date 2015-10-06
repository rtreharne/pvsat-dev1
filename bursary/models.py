from django.db import models
from sorl.thumbnail import ImageField

class Applicant(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    institution = models.CharField(max_length=128)
    supervisor = models.CharField(max_length=128)
    STATUS = (('Awaiting Decision', 'Awaiting decision'), ('Accepted', 'Accept'), ('Rejected', 'Reject') )
    status = models.CharField(max_length=25, choices=STATUS, default='Awaiting Decision')

    def __unicode__(self):
        return self.last_name
