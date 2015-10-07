# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import authors.models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0053_auto_20151007_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 7, 12, 34, 14, 352599)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='upload',
            field=models.FileField(upload_to=b'abstract_uploads', validators=[authors.models.validate_file_extension]),
        ),
    ]
