# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0010_auto_20150716_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='status',
            field=models.CharField(default=b'Awaiting decistion', max_length=25, choices=[(b'Accept', b'Accept'), (b'Reject', b'Reject'), (b'Awaiting Decistion', b'Awaiting decision')]),
        ),
    ]
