from django.db import models
from sorl.thumbnail import ImageField
from time import time
from django.contrib.auth.models import User
from authors.models import UserProfile


class BlogUser(models.Model):
    author = models.ForeignKey(UserProfile)

    def __unicode__(self):
        return self.author.user.last_name

class Article(models.Model):
    author = models.ForeignKey(BlogUser)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    pic = ImageField(upload_to='blog_images', blank=True)

    def __unicode__(self):
        return self.title
