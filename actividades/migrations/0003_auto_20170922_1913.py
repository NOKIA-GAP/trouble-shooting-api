# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0002_auto_20170921_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='subestado_noc',
            field=models.CharField(blank=True, choices=[(b'Alarmas de HW', b'Alarmas de HW'), (b'Alarmas de Rx Sistema Radiante', b'Alarmas de Rx Sistema Radiante'), (b'Alarmas de TX', b'Alarmas de TX'), (b'Alto RTWP', b'Alto RTWP'), (b'Degradacion KPI', b'Degradacion KPI'), (b'Error Comisionamiento BTS', b'Error Comisionamiento BTS'), (b'Error Configuracion Acceso', b'Error Configuracion Acceso'), (b'Error de Instalacion', b'Error de Instalacion'), (b'Pendiente CRQ', b'Pendiente CRQ'), (b'Pendiente DF', b'Pendiente DF'), (b'Pendiente Evidencias', b'Pendiente Evidencias'), (b'Pendiente Pruebas Alarmas', b'Pendiente Pruebas Alarmas'), (b'Pendiente Sitio Limpio', b'Pendiente Sitio Limpio'), (b'Pendiente Tareas Remedy', b'Pendiente Tareas Remedy'), (b'Pendiente Testgestion', b'Pendiente Testgestion'), (b'Perdida de Paquetes', b'Perdida de Paquetes'), (b'Produccion', b'Produccion'), (b'Revision Parcial', b'Revision Parcial'), (b'Seguimiento FO', b'Seguimiento FO'), (b'Sin Trafico', b'Sin Trafico'), (b'Sitio Fuera de Servicio', b'Sitio Fuera de Servicio'), (b'Sin Conexion Remota', b'Sin Conexion Remota'), (b'Adyacencias Faltantes', b'Adyacencias Faltantes')], max_length=255, null=True),
        ),
    ]
