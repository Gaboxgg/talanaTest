# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='arrendado_en',
            field=models.DateTimeField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='auto',
            name='entregado_en',
            field=models.DateTimeField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='auto',
            name='hoja_vida',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hojadevida',
            name='hoja_vida',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
