# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0017_auto_20150716_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='linkedin',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='url',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='abstract',
            name='delivery',
            field=models.CharField(default=b'Oral', max_length=6, choices=[(b'Oral', b'Oral'), (b'Poster', b'Poster')]),
        ),
    ]
