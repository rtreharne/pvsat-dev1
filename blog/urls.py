from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'blog.views.articles', name='articles'),
    url(r'^(?P<article_id>\d+)/$', 'blog.views.article'),
)
