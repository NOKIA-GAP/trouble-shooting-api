# Generated by Django 2.0 on 2017-12-18 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudeshw', '0011_solicitud_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='hardware',
            field=models.CharField(blank=True, choices=[('', '---------'), ('FSMF', 'FSMF'), ('FPFD', 'FPFD'), ('FTIF', 'FTIF'), ('FXCB', 'FXCB'), ('FXFC', 'FXFC'), ('FRHG', 'FRHG'), ('FRHD', 'FRHD'), ('FRHC', 'FRHC'), ('FTSI', 'FTSI'), ('FSFC', 'FSFC'), ('FYTG', 'FYTG'), ('FSEB', 'FSEB'), ('FSES', 'FSES'), ('FBBA', 'FBBA'), ('RET KIT', 'RET KIT'), ('ANTENA', 'ANTENA'), ('JUMPER', 'JUMPER'), ('FEEDER', 'FEEDER'), ('FIBRA', 'FIBRA'), ('FILTRO', 'FILTRO')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='solicitudhw',
            name='estado_solicitud',
            field=models.CharField(blank=True, choices=[('Requiere HW', 'Requiere HW'), ('HW solicitado', 'HW solicitado'), ('HW recibido', 'HW recibido')], default='Requiere HW', max_length=255, null=True),
        ),
    ]
