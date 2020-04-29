# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_auto_20200429_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='modelo',
            field=models.CharField(default='', max_length=100),
        ),
    ]
