# Generated by Django 2.2.7 on 2020-01-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_stationdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationdetails',
            name='dateofupload',
            field=models.DateField(auto_now_add=True),
        ),
    ]
