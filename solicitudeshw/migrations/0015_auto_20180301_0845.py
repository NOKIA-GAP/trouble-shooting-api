# Generated by Django 2.0 on 2018-03-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudeshw', '0014_auto_20180213_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='hardware',
            field=models.CharField(blank=True, choices=[('', '---------'), ('FSMF', 'FSMF'), ('FPFD', 'FPFD'), ('FTIF', 'FTIF'), ('FXCB', 'FXCB'), ('FXFC', 'FXFC'), ('FRHG', 'FRHG'), ('FRHD', 'FRHD'), ('FRHC', 'FRHC'), ('FTSI', 'FTSI'), ('FSFC', 'FSFC'), ('FYTG', 'FYTG'), ('FSEB', 'FSEB'), ('FSES', 'FSES'), ('FBBA', 'FBBA'), ('RET KIT', 'RET KIT'), ('ANTENA', 'ANTENA'), ('JUMPER', 'JUMPER'), ('FEEDER', 'FEEDER'), ('FIBRA', 'FIBRA'), ('FILTRO', 'FILTRO'), ('OVP', 'OVP')], max_length=255, null=True),
        ),
    ]