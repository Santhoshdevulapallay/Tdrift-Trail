# Generated by Django 2.2.7 on 2019-11-29 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_authentication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authentication',
            name='password',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='authentication',
            name='username',
            field=models.CharField(max_length=25),
        ),
    ]