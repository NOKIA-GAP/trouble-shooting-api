# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='perfil_usuario',
            field=models.CharField(blank=True, choices=[(b'NI Ingeniero', b'NI Ingeniero'), (b'NI Asignador', b'NI Asignador'), (b'NPO Ingeniero', b'NPO Ingeniero'), (b'NPO Asignador', b'NPO Asignador'), (b'FM Lider', b'FM Lider'), (b'FM Permisos', b'FM Permisos')], max_length=255, null=True),
        ),
    ]
