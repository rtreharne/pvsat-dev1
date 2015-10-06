# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0006_auto_20150715_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='status',
            field=models.CharField(default=b'AWAIT', max_length=3, choices=[(b'ACCEPT', b'Accept'), (b'REJECT', b'Reject'), (b'AWAIT', b'Awaiting decision')]),
        ),
    ]
