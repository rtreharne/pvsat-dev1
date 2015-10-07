# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0052_auto_20151007_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 7, 12, 21, 32, 499220)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='upload',
            field=models.FileField(upload_to=b'abstract_uploads'),
        ),
    ]
