# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-18 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0023_auto_20171017_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='estado_noc',
            field=models.CharField(blank=True, choices=[(b'Produccion', b'Produccion'), (b'Escalado a Implementacion', b'Escalado a Implementacion'), (b'Escalado a Grupo Calidad', b'Escalado a Grupo Calidad'), (b'Escalado a RF', b'Escalado a RF'), (b'Escalado a OyM', b'Escalado a OyM'), (b'Escalado a GDRT', b'Escalado a GDRT'), (b'Escalado Control Cambios', b'Escalado Control Cambios'), (b'Seguimiento 12h', b'Seguimiento 12h'), (b'Seguimiento 24h', b'Seguimiento 24h'), (b'Seguimiento 36h', b'Seguimiento 36h'), (b'Seguimiento FO', b'Seguimiento FO'), (b'PreCheck', b'PreCheckC'), (b'Pendiente Remedy', b'Pendiente Remedy'), (b'Stand By', b'Stand By'), (b'Rollback', b'Rollback'), (b'Suspendido', b'Suspendido')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='subestado_noc',
            field=models.CharField(blank=True, choices=[(b'Alarmas', b'Alarmas'), (b'Alarmas de HW', b'Alarmas de HW'), (b'Alarmas de Rx Sistema Radiante', b'Alarmas de Rx Sistema Radiante'), (b'Alarmas de TX', b'Alarmas de TX'), (b'Alarmas de energia', b'Alarmas de energia'), (b'Alarmas TRAFFIC CHAN', b'Alarmas TRAFFIC CHAN'), (b'Alto RTWP', b'Alto RTWP'), (b'Causa Externa', b'Causa Externa'), (b'Degradacion KPI', b'Degradacion KPI'), (b'Error Comisionamiento BTS', b'Error Comisionamiento BTS'), (b'Error Configuracion Acceso', b'Error Configuracion Acceso'), (b'Error de Instalacion', b'Error de Instalacion'), (b'Error comisionamiento BTS', b'Error comisionamiento BTS'), (b'Error configuracion Acceso', b'Error configuracion Acceso'), (b'Error de instalacion', b'Error de instalacion'), (b'Fuera de servicio', b'Fuera de servicio'), (b'Produccion', b'Produccion'), (b'Pendiente CRQ', b'Pendiente CRQ'), (b'Pendiente DF', b'Pendiente DF'), (b'Pendiente Evidencias', b'Pendiente Evidencias'), (b'Pendiente Pruebas Alarmas', b'Pendiente Pruebas Alarmas'), (b'Pendiente Sitio Limpio', b'Pendiente Sitio Limpio'), (b'Pendiente Tareas Remedy', b'Pendiente Tareas Remedy'), (b'Pendiente Testgestion', b'Pendiente Testgestion'), (b'Pendiente Remedy', b'Pendiente Remedy'), (b'Pendiente Actualizacion DF', b'Pendiente Actualizacion DF'), (b'Pendiente Notificacion', b'Pendiente Notificacion'), (b'Perdida de Paquetes', b'Perdida de Paquetes'), (b'Produccion', b'Produccion'), (b'Revision Parcial', b'Revision Parcial'), (b'Reinicio 12Hrs', b'Reinicio 12Hrs'), (b'Seguimiento 12H', b'Seguimiento 12H'), (b'Seguimiento 24H', b'Seguimiento 24H'), (b'Seguimiento 36H', b'Seguimiento 36H'), (b'Precheck', b'Precheck'), (b'Sin Trafico', b'Sin Trafico'), (b'Sitio Fuera de Servicio', b'Sitio Fuera de Servicio'), (b'Sin Conexion Remota', b'Sin Conexion Remota'), (b'Stand By', b'Stand By'), (b'Adyacencias Faltantes', b'Adyacencias Faltantes')], max_length=255, null=True),
        ),
    ]
