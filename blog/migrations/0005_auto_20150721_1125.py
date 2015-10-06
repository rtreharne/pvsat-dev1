# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_bloguser_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloguser',
            name='test',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='blog.BlogUser'),
        ),
    ]
