# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-04 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudeshw', '0003_auto_20171204_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware', models.CharField(blank=True, max_length=255, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('estado', models.BooleanField(default=False, editable=False)),
                ('subestado', models.BooleanField(default=False, editable=False)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('solicitudhw', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='solicitudeshw.SolicitudHW')),
            ],
            options={
                'ordering': ('creado',),
                'verbose_name': 'solicitud',
                'verbose_name_plural': 'solicitudes',
            },
        ),
    ]
