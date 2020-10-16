from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from owid.text_owid import *
from owid.models import *
from django.utils import timezone
from datetime import *
from owid.text_owid import *
from owid.service import *
import owid.service_covid as service_covid
import owid.service_owid as service_owid


def tests(request):
    return render(request, 'owid/test.html', {})


def index(request):
    context = service_owid.get_index_context()
    return render(request, 'owid/index.html', context)


def covid(request):
    context = service_covid.get_covid_selection_data()
    return render(request, 'owid/covid.html', context)


def country(request):
    if request.method == "POST":
        location = request.POST['location']
    else:
        location = 'World'
    context = service_covid.get_country_data(location)
    return render(request, 'owid/country.html', context)


def world(request):
    location = 'World'
    context = service_covid.get_country_data(location)
    return render(request, 'owid/country.html', context)


def charts_bar_newcases_world(request):
    location = 'World'
    context = service_covid.get_newcases_all(location)
    return render(request, 'owid/charts_covid_bar.html', context)


def charts_bar_newcases_country(request):
    location = request.POST['location']
    locations = service_covid.get_location_list()
    if location not in locations:
        return render(request, 'owid/covid.html', {
            'locations': locations,
            'error_message': "You didn't select a country."})
    else:
        context = service_covid.get_newcases_all(location)
        return render(request, 'owid/charts_covid_bar.html', context)


def charts_bar_totalcases_country(request):
    location = request.POST['location']
    locations = service_covid.get_location_list()
    if location not in locations:
        return render(request, 'owid/covid.html', {
            'locations': locations,
            'error_message': "You didn't select a country."})
    else:
        context = service_covid.get_totalcases_all(location)
        return render(request, 'owid/charts_covid_line.html', context)


def charts_bar_newdeaths_country(request):
    location = request.POST['location']
    locations = service_covid.get_location_list()
    if location not in locations:
        return render(request, 'owid/covid.html', {
            'locations': locations,
            'error_message': "You didn't select a country."})
    else:
        context = service_covid.get_newdeaths_all(location)
        return render(request, 'owid/charts_covid_bar.html', context)


def charts_bar_totaldeaths_country(request):
    location = request.POST['location']
    locations = service_covid.get_location_list()
    if location not in locations:
        return render(request, 'owid/covid.html', {
            'locations': locations,
            'error_message': "You didn't select a country."})
    else:
        context = service_covid.get_totaldeaths_all(location)
        return render(request, 'owid/charts_covid_line.html', context)


# ----------- old -----------------


def charts_pl_newcases_bar(request):
    context = service_covid.get_pl_newcases_all()
    return render(request, 'owid/charts_covid_bar.html', context)


def charts_pl_totalcases_bar(request):
    context = service_covid.get_pl_totalcases_all()
    return render(request, 'owid/charts_covid_bar.html', context)


def charts_pl_newdeaths_bar(request):
    context = service_covid.get_pl_newdeaths_all()
    return render(request, 'owid/charts_covid_bar.html', context)


def charts_pl_totaldeaths_bar(request):
    context = service_covid.get_pl_totaldeaths_all()
    return render(request, 'owid/charts_covid_bar.html', context)


def test(request):
    countries = Country.objects.using('owid')[:30]
    print(countries)
    locations = [c.location for c in countries]
    print(locations)
    context = {'locations': locations,
               'countries': countries}
    return render(request, 'owid/test.html', context)
