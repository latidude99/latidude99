from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tests', views.tests, name='tests'),
    path('covid', views.covid, name='covid'),
    path('covid/country', views.country, name='country'),
    path('covid/country/barcharts/newcases/', views.charts_bar_newcases_country,
         name='charts_bar_newcases_country'),
    path('covid/country/barcharts/totalcases/', views.charts_bar_totalcases_country,
         name='charts_bar_totalcases_country'),
    path('covid/country/barcharts/newdeaths/', views.charts_bar_newdeaths_country,
         name='charts_bar_newdeaths_country'),
    path('covid/country/barcharts/totaldeaths/', views.charts_bar_totaldeaths_country,
         name='charts_bar_totaldeaths_country'),

    path('charts_bar_newcases_world/newcases/', views.charts_bar_newcases_world,
         name='charts_bar_newcases_world'),

    path('charts_covid_bar/pl/newcases', views.charts_pl_newcases_bar, name='charts_pl_newcases_bar'),
    path('charts_covid_bar/pl/totalcases', views.charts_pl_totalcases_bar, name='charts_pl_totalcases_bar'),
    path('charts_covid_bar.html/pl/newdeaths', views.charts_pl_newdeaths_bar, name='charts_pl_newdeaths_bar'),
    path('charts_covid_bar.html/pl/totaldeaths', views.charts_pl_totaldeaths_bar, name='charts_pl_totaldeaths_bar'),

]
