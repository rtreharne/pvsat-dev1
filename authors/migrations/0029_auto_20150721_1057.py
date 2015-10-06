# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0028_auto_20150721_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 10, 57, 52, 836231)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='affiliation',
            field=models.CharField(max_length=128, blank=True),
        ),
    ]
