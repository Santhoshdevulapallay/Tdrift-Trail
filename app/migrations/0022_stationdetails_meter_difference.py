# Generated by Django 2.2.7 on 2019-12-18 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_stationdetails_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='stationdetails',
            name='meter_difference',
            field=models.CharField(default='Null', max_length=55),
        ),
    ]