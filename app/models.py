from django.db import models
from django.conf import settings
from django.db import models
from datetime import date,datetime

class StationDetails(models.Model):
    utility_name=models.CharField(max_length=255,default="NULL")
    station_name=models.CharField(max_length=255,null=False)
    Meter_no=models.CharField(max_length=255,null=False)
    description=models.CharField(max_length=255,null=True)
    gps=models.TimeField(max_length=50,auto_now_add=False)
    meter_drift=models.TimeField(max_length=50,null=False,auto_now_add=False)
    meter_difference=models.TimeField(max_length=55,null=False,auto_now_add=False)
    meter_status=models.CharField(max_length=15,default='NULL')
    dateofchecking=models.DateField(auto_now_add=False)
    dateofupload=models.DateField(auto_now_add=False)
    correction_needed=models.CharField(max_length=20,choices=(
        ('yes','Yes'),
        ('no','No')
    ))
    remarks=models.CharField(max_length=200)
    def __str__(self):
        return self.station_name
# class Station(models.Model):
    # name=models.CharField(max_length=35)
    # address=models.CharField(max_length=65)
class Authentication(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)   
    def __str__(self):
        return self.username
class Station_store(models.Model):
    utility_name=models.CharField(max_length=25)
    station_name=models.CharField(max_length=25)
    location_name=models.CharField(max_length=50,default='Null')
    def __str__(self):
        return self.utility_name
    
# Create your models here.
class Semlog_data(models.Model):
    Utility_Name=models.CharField(max_length=255)
    Station_Name=models.TextField()
    Location=models.TextField()
    Description=models.TextField()
    Meter_No=models.CharField(max_length=255)

    def __str__(self):
        return self.Station_Name
photo = models.ImageField(upload_to="gallery")   