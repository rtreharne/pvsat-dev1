# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0002_remove_speaker_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='affiliation',
            field=models.CharField(max_length=128),
        ),
    ]
