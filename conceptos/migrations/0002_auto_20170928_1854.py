# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 23:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conceptos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asignacionconceptoni',
            options={'ordering': ('creado',), 'verbose_name': 'asignacion concepto ni', 'verbose_name_plural': 'asignacion conceptos ni'},
        ),
        migrations.AlterModelOptions(
            name='asignacionconceptonpo',
            options={'ordering': ('creado',), 'verbose_name': 'asignacion concepto npo', 'verbose_name_plural': 'asignacion conceptos npo'},
        ),
    ]
