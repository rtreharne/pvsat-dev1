# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0061_auto_20151007_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='author_registered',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 7, 14, 40, 44, 91385)),
        ),
    ]
