# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('url', models.URLField()),
                ('logo', models.ImageField(upload_to=b'exhibitor_img', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
