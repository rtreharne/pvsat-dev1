# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0058_auto_20151007_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 7, 14, 31, 44, 361831)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='tags',
            field=models.CharField(help_text=b'e.g. CdTe, modeling, liverpool', max_length=250, null=True, blank=True),
        ),
    ]
