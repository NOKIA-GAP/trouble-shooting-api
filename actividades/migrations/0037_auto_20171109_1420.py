# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0036_auto_20171109_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degradacion',
            name='wp',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
