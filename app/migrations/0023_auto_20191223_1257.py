# Generated by Django 2.2.7 on 2019-12-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_stationdetails_meter_difference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationdetails',
            name='Meter_no',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='stationdetails',
            name='meter_difference',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='stationdetails',
            name='meter_drift',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stationdetails',
            name='remarks',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='stationdetails',
            name='station_name',
            field=models.CharField(max_length=65),
        ),
    ]
