# Generated by Django 2.2.7 on 2019-11-26 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191125_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='stationdetails',
            name='station_name',
            field=models.CharField(default='Null', max_length=65),
        ),
    ]
