# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0015_auto_20150716_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='status',
            field=models.CharField(default=b'Awaiting decistion', max_length=25, choices=[(b'Accepted', b'Accept'), (b'Rejected', b'Reject'), (b'Awaiting Decision', b'Awaiting decision')]),
        ),
    ]
