# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0005_auto_20150715_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abstract',
            old_name='accept',
            new_name='status',
        ),
    ]
