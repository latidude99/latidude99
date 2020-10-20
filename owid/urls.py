from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tests', views.tests, name='tests'),
    path('covid', views.covid, name='covid'),
    path('covid/country', views.country, name='country'),
    path('covid/countries', views.countries, name='countries'),
    path('covid/world', views.world, name='world'),

    path('covid/countries/charts/newcases/', views.charts_newcases_country_group,
         name='charts_newcases_country_group'),
    path('covid/countries/charts/totalcases/', views.charts_totalcases_country_group,
         name='charts_totalcases_country_group'),
    path('covid/countries/charts/newdeaths/', views.charts_newdeaths_country_group,
         name='charts_newdeaths_country_group'),
    path('covid/countries/charts/totaldeaths/', views.charts_totaldeaths_country_group,
         name='charts_totaldeaths_country_group'),

path('covid/countries/charts/newcases100/', views.charts_newcases100_country_group,
         name='charts_newcases100_country_group'),
path('covid/countries/charts/totalcases100/', views.charts_totalcases100_country_group,
         name='charts_totalcases100_country_group'),
path('covid/countries/charts/newdeaths100/', views.charts_newdeaths100_country_group,
         name='charts_newdeaths100_country_group'),
path('covid/countries/charts/totaldeaths100/', views.charts_totaldeaths100_country_group,
         name='charts_totaldeaths100_country_group'),

    path('covid/country/charts/newcases/', views.charts_bar_newcases_country,
         name='charts_bar_newcases_country'),
    path('covid/country/charts/totalcases/', views.charts_bar_totalcases_country,
         name='charts_bar_totalcases_country'),
    path('covid/country/charts/newdeaths/', views.charts_bar_newdeaths_country,
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
