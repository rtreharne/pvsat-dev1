# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0009_auto_20150716_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='status',
            field=models.CharField(default=b'Awaiting decistion', max_length=25, choices=[(b'ACCEPT', b'Accept'), (b'REJECT', b'Reject'), (b'AWAIT', b'Awaiting decision')]),
        ),
    ]
