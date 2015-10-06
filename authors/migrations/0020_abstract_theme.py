# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0002_theme'),
        ('authors', '0019_userprofile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstract',
            name='theme',
            field=models.ManyToManyField(to='programme.Theme'),
            preserve_default=True,
        ),
    ]
