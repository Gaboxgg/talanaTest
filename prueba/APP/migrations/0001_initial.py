# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tamano', models.CharField(max_length=100)),
                ('puertas', models.CharField(max_length=300)),
                ('diesel', models.CharField(max_length=300)),
                ('hoja_vida', models.CharField(max_length=300)),
                ('arrendado_en', models.DateTimeField(max_length=100)),
                ('entregado_en', models.DateTimeField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('rut', models.CharField(max_length=300)),
                ('clave', models.CharField(max_length=300)),
                ('autos_arredandos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HojaDeVida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hoja_vida', models.CharField(max_length=300)),
                ('creado_en', models.DateTimeField(max_length=100)),
                ('auto', models.ForeignKey(to='APP.Auto')),
                ('cliente', models.ForeignKey(to='APP.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creado_en', models.DateTimeField(max_length=100)),
                ('auto', models.ForeignKey(to='APP.Auto')),
                ('cliente', models.ForeignKey(to='APP.Cliente')),
            ],
        ),
    ]
