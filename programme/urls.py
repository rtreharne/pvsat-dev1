from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'programme.views.programme', name='programme'),
	url(r'^abstracts/$', 'programme.views.abstracts', name='abstracts'),
    url(r'^abstracts/(?P<abstract_id>\d+)/$', 'programme.views.abstract'),
    url(r'^profiles/(?P<user_id>\d+)/$', 'programme.views.profile'),
    url(r'^themes/(?P<theme_id>\d+)/$', 'programme.views.theme'),
)
