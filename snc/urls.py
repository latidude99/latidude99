from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('charts', views.charts, name='charts'),
    path('charts/<int:scale>/', views.charts, name='charts'),
    path('chartdetails', views.chartdetails, name='chartdetails'),

    path('charts_file', views.charts_file, name='charts_file'),
    path('admin', views.admin, name='user'),
    path('info', views.info, name='info'),
    path('charts_all', views.charts_all, name='charts_all'),

    path('multisearch', views.multisearch, name='multisearch'),

]

