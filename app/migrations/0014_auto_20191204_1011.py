# Generated by Django 2.2.7 on 2019-12-04 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20191204_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationdetails',
            name='dateofchecking',
            field=models.DateField(),
        ),
    ]
