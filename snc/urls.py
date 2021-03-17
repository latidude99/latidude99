from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('charts', views.charts, name='charts'),
    path('admin', views.admin, name='user'),
    path('info', views.info, name='info'),
    path('charts_all', views.charts_all, name='charts_all'),

    path('charts_1', views.charts_1, name='charts_1'),
    path('charts_2', views.charts_2, name='charts_2'),
    path('charts_3', views.charts_3, name='charts_3'),
    path('charts_4', views.charts_4, name='charts_4'),
    path('charts_5', views.charts_5, name='charts_5'),
    path('charts_6', views.charts_6, name='charts_6'),
    path('charts_7', views.charts_7, name='charts_7'),

    path('multisearch', views.multisearch, name='multisearch'),

]

