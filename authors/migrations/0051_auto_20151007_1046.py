# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0050_auto_20151005_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='unique_id',
            field=models.CharField(max_length=9, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 7, 10, 46, 55, 535921)),
        ),
    ]
