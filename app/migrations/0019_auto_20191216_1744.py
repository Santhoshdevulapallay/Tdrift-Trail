# Generated by Django 2.2.7 on 2019-12-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_semlog_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semlog_data',
            name='Description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='semlog_data',
            name='Location',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='semlog_data',
            name='Meter_No',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='semlog_data',
            name='Station_Name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='semlog_data',
            name='Utility_Name',
            field=models.CharField(max_length=255),
        ),
    ]
