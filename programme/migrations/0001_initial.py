# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('forename', models.CharField(unique=True, max_length=128)),
                ('surname', models.CharField(unique=True, max_length=128)),
                ('affiliation', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128, blank=True)),
                ('pic', sorl.thumbnail.fields.ImageField(upload_to=b'logo_images', blank=True)),
                ('url', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
