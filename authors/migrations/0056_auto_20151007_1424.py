# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0055_auto_20151007_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='tags',
            field=models.CharField(default='default', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='abstract',
            name='abstract',
            field=models.TextField(help_text=b'Pasting your abstract text will help us make your work searchable.', max_length=50000),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 7, 14, 24, 28, 504636)),
        ),
    ]
