# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-11 03:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0039_auto_20171110_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='responsable',
        ),
    ]
