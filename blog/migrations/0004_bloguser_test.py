# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_bloguser'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='test',
            field=models.CharField(default='', max_length=12),
            preserve_default=False,
        ),
    ]
