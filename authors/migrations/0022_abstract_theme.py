# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0002_theme'),
        ('authors', '0021_remove_abstract_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='theme',
            field=models.ManyToManyField(to='programme.Theme'),
            preserve_default=True,
        ),
    ]
