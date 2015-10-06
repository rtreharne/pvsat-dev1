# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0020_abstract_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abstract',
            name='theme',
        ),
    ]
