# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-11 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estaciones', '0006_auto_20171110_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacion',
            name='prioridad',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
