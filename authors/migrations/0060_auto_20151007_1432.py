# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0059_auto_20151007_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 7, 14, 32, 32, 14335)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='tags',
            field=models.CharField(help_text=b'e.g. CdTe, modeling, liverpool', max_length=250),
        ),
    ]
