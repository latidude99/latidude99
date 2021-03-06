from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tests', views.tests, name='tests'),

    path('cia', views.cia, name='cia'),
    path('cia_country', views.cia_country, name='cia_country'),

    path('covid', views.covid, name='covid'),
    path('covid/tasks', views.tasks_owid, name='tasks_owid'),

    path('covid/numbers', views.numbers, name='numbers'),
    path('covid/flrace_cases20', views.flrace_cases20, name='flrace_cases20'),
    path('covid/flrace_deaths20', views.flrace_deaths20, name='flrace_deaths20'),
    path('covid/flrace_cases40', views.flrace_cases40, name='flrace_cases40'),
    path('covid/flrace_deaths40', views.flrace_deaths40, name='flrace_deaths40'),
    path('covid/flrace_cases20_100', views.flrace_cases20_100, name='flrace_cases20_100'),
    path('covid/flrace_deaths20_100', views.flrace_deaths20_100, name='flrace_deaths20_100'),
    path('covid/flrace_cases40_100', views.flrace_cases40_100, name='flrace_cases40_100'),
    path('covid/flrace_deaths40_100', views.flrace_deaths40_100, name='flrace_deaths40_100'),

    path('covid/numbers/country_json', views.country_json, name='country_json'),
    path('covid/numbers/country_json_chart', views.country_json_chart, name='country_json_chart'),
    path('covid/numbers_json', views.numbers_json, name='numbers_json'),

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
    path('covid/country/charts/totalcases/', views.charts_line_totalcases_country,
         name='charts_line_totalcases_country'),
    path('covid/country/charts/newdeaths/', views.charts_bar_newdeaths_country,
         name='charts_bar_newdeaths_country'),
    path('covid/country/barcharts/totaldeaths/', views.charts_line_totaldeaths_country,
         name='charts_line_totaldeaths_country'),

    path('charts_bar_newcases_world/newcases/', views.charts_bar_newcases_world,
         name='charts_bar_newcases_world'),

]
