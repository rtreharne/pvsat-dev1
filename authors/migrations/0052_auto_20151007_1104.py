# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0051_auto_20151007_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 7, 11, 4, 46, 727742)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='unique_id',
            field=models.CharField(max_length=11, unique=True, null=True, blank=True),
        ),
    ]
