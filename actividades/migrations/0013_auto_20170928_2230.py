# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 03:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0012_auto_20170928_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conceptoni',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='conceptoni',
            name='estacion',
        ),
        migrations.RemoveField(
            model_name='conceptoni',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='conceptoni',
            name='user',
        ),
        migrations.RemoveField(
            model_name='conceptonpo',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='conceptonpo',
            name='estacion',
        ),
        migrations.RemoveField(
            model_name='conceptonpo',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='conceptonpo',
            name='user',
        ),
        migrations.DeleteModel(
            name='ConceptoNi',
        ),
        migrations.DeleteModel(
            name='ConceptoNpo',
        ),
    ]
