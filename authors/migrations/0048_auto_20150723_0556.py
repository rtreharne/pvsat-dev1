# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0047_auto_20150722_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 5, 56, 38, 215037)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=sorl.thumbnail.fields.ImageField(default=b'static/img/avatar.png', upload_to=b'user_images'),
        ),
    ]
