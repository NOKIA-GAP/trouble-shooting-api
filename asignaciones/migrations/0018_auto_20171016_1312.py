# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 18:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asignaciones', '0017_auto_20171013_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asignacionni',
            old_name='estado',
            new_name='estado_asignacion',
        ),
        migrations.RenameField(
            model_name='asignacionnpo',
            old_name='estado',
            new_name='estado_asignacion',
        ),
    ]
