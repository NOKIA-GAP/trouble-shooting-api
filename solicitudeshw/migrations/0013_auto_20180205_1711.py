# Generated by Django 2.0 on 2018-02-05 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudeshw', '0012_auto_20171217_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudhw',
            name='estado_solicitud',
            field=models.CharField(blank=True, choices=[('Requiere HW', 'Requiere HW'), ('HW solicitado', 'HW solicitado'), ('HW recibido', 'HW recibido'), ('Cancelada', 'Cancelada')], default='Requiere HW', max_length=255, null=True),
        ),
    ]
