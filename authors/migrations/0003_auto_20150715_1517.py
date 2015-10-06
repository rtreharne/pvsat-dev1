# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_abstract'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abstract',
            old_name='user',
            new_name='author',
        ),
    ]
