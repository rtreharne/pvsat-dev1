# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bursary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='status',
            field=models.CharField(default=b'Awaiting Decision', max_length=25, choices=[(b'Awaiting Decision', b'Awaiting decision'), (b'Accepted', b'Accept'), (b'Rejected', b'Reject')]),
            preserve_default=True,
        ),
    ]
