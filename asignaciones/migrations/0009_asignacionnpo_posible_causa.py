# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignaciones', '0008_auto_20171010_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacionnpo',
            name='posible_causa',
            field=models.CharField(blank=True, choices=[(b'', b''), (b'', b''), (b'', b''), (b'', b''), (b'', b'')], max_length=255, null=True),
        ),
    ]
