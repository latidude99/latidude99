from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('charts', views.charts, name='charts'),
    path('chs', views.chs, name='chs'),

    path('charts/<int:scale>/', views.charts, name='charts'),
    path('chartdetails', views.chartdetails, name='chartdetails'),
    path('chartgeojson', views.chartgeojson, name='chartgeojson'),
    path('chartgeojson8XXX', views.chartgeojson8XXX, name='chartgeojson8XXX'),

    path('charts_file', views.charts_file, name='charts_file'),
    path('charts_chs_file', views.charts_chs_file, name='charts_chs_file'),
    path('admin', views.admin, name='user'),
    path('info', views.info, name='info'),
    path('charts_all', views.charts_all, name='charts_all'),

    path('multisearch', views.multisearch, name='multisearch'),

    path('download_catalogue_latest', views.download_catalogue_latest, name='download_catalogue_latest'),

]

