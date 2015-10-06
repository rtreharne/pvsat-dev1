# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0022_abstract_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='author',
            field=models.ForeignKey(to='authors.UserProfile'),
        ),
    ]
