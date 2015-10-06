# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_auto_20150715_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='abstract',
            field=models.TextField(max_length=5000),
        ),
    ]
