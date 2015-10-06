# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0023_auto_20150716_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 19, 18, 11, 49, 147813)),
            preserve_default=True,
        ),
    ]
