# Generated by Django 2.0 on 2018-01-12 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asignaciones', '0035_asignacionni_asignar_par'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacionni',
            name='detalle_solicitud_visita',
            field=models.TextField(blank=True, null=True),
        ),
    ]
