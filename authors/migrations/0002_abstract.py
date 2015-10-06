# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abstract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000)),
                ('abstract', models.TextField(max_length=5000, blank=True)),
                ('upload', models.FileField(upload_to=b'abstract_uploads', blank=True)),
                ('delivery', models.CharField(default=b'OR', max_length=2, choices=[(b'OR', b'Oral'), (b'PO', b'Poster')])),
                ('accept', models.CharField(default=b'NO', max_length=3, choices=[(b'YES', b'Yes'), (b'NO', b'No')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
