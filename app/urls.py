from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.views.generic.base import TemplateView
app_name='app'
urlpatterns=[
    # path('password_reset/subscribe',views.subscribe),
    path('upload',views.upload),
    path('uploaded_file',views.uploaded_file),
    path('submitform',views.formsubmit),
    path('file_user',views.user_fileupload),
    path('stationdata',views.stationdata),
    path('home', views.home_page),
    path('file_format',views.file_format),
    path('fulldetails',views.station_finaldata),
    path('meterdetails',views.meter_details),
    path('month_detailspage',views.month_detailspage),
    path('month_wise',views.month_wise),
    path('date_wisedetails',views.date_wise),
    path('daterange',views.date_range1),
    path('stationlist',views.station_fetch),
    path('add_station',views.add_station),
    path('adding_station',views.adding_station),
    path('excel_download',views.download_excel_data),
    path('date_excel_download',views.date_wise_excel),
    path('excel_upload',TemplateView.as_view(template_name='excel_upload.html')),
    path('monthlyfile_status',TemplateView.as_view(template_name='monthlyfile_status.html')),
    path('powergrid_month',TemplateView.as_view(template_name='powergrid_month.html')),
    path('drift_details',TemplateView.as_view(template_name='drift_details.html')),
    path('powergrid_status',TemplateView.as_view(template_name='powergrid_status.html')),
    path('final_filestatus',views.final_status),
    path('drift_range',views.drift_range),
    path('drift_excel_download',views.drift_excel_download),
   # path('home1',views.home1),
]