# Generated by Django 2.0 on 2018-01-24 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidentes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidenteni',
            name='asignar_par',
            field=models.BooleanField(default=False),
        ),
    ]
