# Generated by Django 2.2.7 on 2019-12-03 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20191203_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationdetails',
            name='dateofchecking',
            field=models.CharField(default='Null', max_length=50),
        ),
    ]
