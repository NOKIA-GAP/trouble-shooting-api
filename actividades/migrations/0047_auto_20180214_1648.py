# Generated by Django 2.0 on 2018-02-14 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0046_auto_20180202_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='tipo_trabajo',
            field=models.CharField(blank=True, choices=[('LTE Overlay', 'LTE Overlay'), ('Tercera Portadora', 'Tercera Portadora'), ('3G Huawei Overlay', '3G Huawei Overlay'), ('Sitio Nuevo 3G', 'Sitio Nuevo 3G'), ('Sitio Nuevo 2G PE', 'Sitio Nuevo 2G PE'), ('Sitio Nuevo LTE', 'Sitio Nuevo LTE'), ('Sector Expansion', 'Sector Expansion'), ('Sitio Nuevo 3G PE', 'Sitio Nuevo 3G PE'), ('3G Overlay', '3G Overlay'), ('Cambio de Jumpers y Breaker_CP', 'Cambio de Jumpers y Breaker_CP'), ('Cambio HW para MC_CP', 'Cambio HW para MC_CP'), ('Channel Element_CP', 'Channel Element_CP'), ('Adecuaciones LTE', 'Adecuaciones LTE'), ('Cuarta Portadora', 'Cuarta Portadora'), ('Cambio HW para MC', 'Cambio HW para MC'), ('Modernizacion Multiradio', 'Modernizacion Multiradio'), ('Channel Element_MMR', 'Channel Element_MMR'), ('Segundo Nodo', 'Segundo Nodo'), ('Channel Element_5P', 'Channel Element_5P'), ('Reubicacion', 'Reubicacion'), ('Sitio Nuevo LTE PE', 'Sitio Nuevo LTE PE'), ('Sector Expansion Huawei', 'Sector Expansion Huawei'), ('Cambio de Jumpers y RRU', 'Cambio de Jumpers y RRU'), ('Cambio HW para MC Huawei', 'Cambio HW para MC Huawei'), ('Swap', 'Swap'), ('Cambio HW LTE', 'Cambio HW LTE'), ('Sitio Nuevo 3G/LTE Temporal', 'Sitio Nuevo 3G/LTE Temporal'), ('Cambio de Jumpers y Breaker', 'Cambio de Jumpers y Breaker'), ('Cambio de Jumpers y Breaker_5P', 'Cambio de Jumpers y Breaker_5P'), ('Adecuaciones SE', 'Adecuaciones SE'), ('LTE Huawei Overlay', 'LTE Huawei Overlay'), ('Adecuaciones LTE Huawei', 'Adecuaciones LTE Huawei'), ('Channel Element', 'Channel Element'), ('Cambio HW para MC_5P', 'Cambio HW para MC_5P'), ('Cambio HW para MC_5P y RF', 'Cambio HW para MC_5P y RF'), ('Swap Antenas Capa 4-5', 'Swap Antenas Capa 4-5'), ('Channel Element + Upgrade Modulos RF', 'Channel Element + Upgrade Modulos RF'), ('Channel Element_5P y RF', 'Channel Element_5P y RF'), ('Cuarta Portadora Huawei', 'Cuarta Portadora Huawei'), ('Tercera Portadora Huawei', 'Tercera Portadora Huawei'), ('Adecuaciones Overlay', 'Adecuaciones Overlay'), ('Adecuacion para LTE 1900Mhz', 'Adecuacion para LTE 1900Mhz'), ('Upgrade Modulos RF', 'Upgrade Modulos RF'), ('Cambio Feeder a Fibra', 'Cambio Feeder a Fibra'), ('RF Sharing a Dedicado', 'RF Sharing a Dedicado'), ('Reubicacion Equipos', 'Reubicacion Equipos'), ('Cambio HW', 'Cambio HW'), ('Modernizacion Concurrente', 'Modernizacion Concurrente'), ('Cambio de Jumpers', 'Cambio de Jumpers'), ('2G Overlay', '2G Overlay')], max_length=255, null=True),
        ),
    ]