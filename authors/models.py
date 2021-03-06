from django.db import models
from django.contrib.auth.models import User
from programme.models import Theme
from django.utils import timezone
from time import time
from sorl.thumbnail import get_thumbnail, ImageField
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.doc', '.docx']
    filesize = value.file.size
    if filesize > 10*1024*1024:
        raise ValidationError(u'Max file size 10MB.')
    if not ext in valid_extensions:
        raise ValidationError(u'File must not supported. Files must be .doc or .docx')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    affiliation = models.CharField(max_length=128, blank = True)
    picture = ImageField(upload_to='user_images', default='static/img/avatar.png')
    url = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    bio = models.TextField(max_length=2000, blank=True)

    def __unicode__(self):
        return self.user.username

class Abstract(models.Model):
    
    help = "Pasting your abstract text will help us make your work searchable."


    author = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=1000)
    abstract = models.TextField(max_length=50000, help_text = help)
    upload = models.FileField(upload_to='abstract_uploads', validators=[validate_file_extension])
    theme = models.ManyToManyField(Theme)
    unique_id = models.CharField(max_length=11,null=True, blank=True, unique=True)
    
    DELIVERY_CHOICE = (('Oral', 'Oral'), ('Poster', 'Poster'))
    delivery = models.CharField(max_length=6, choices=DELIVERY_CHOICE, default='Oral')

    STATUS = (('Awaiting Decision', 'Awaiting decision'), ('Accepted', 'Accept'), ('Rejected', 'Reject') )
    status = models.CharField(max_length=25, choices=STATUS, default='Awaiting Decision')

    date = models.DateTimeField(default=timezone.datetime.today())
    tags = models.CharField(max_length=250, help_text = "e.g. CdTe, modeling, liverpool")
    author_registered = models.BooleanField(default=False)


    def __unicode__(self):
        return self.title
    


