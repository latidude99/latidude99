from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

import owid.service as service
import owid.service_covid as service_covid
import owid.service_owid as service_owid
from main.secrets import *
import latidude99.tasks as tasks


def tests(request):
    return render(request, 'owid/test.html', {})


def index(request):
    context = service_owid.get_index_context()
    return render(request, 'owid/index.html', context)


def tasks_owid(request):
    ctx = {}
    if request.method == "POST":
        login = request.POST['login']
        pswd = request.POST['pswd']
        task = request.POST['task']
        print(task)
        if login == COVID_TASKS_LOGIN and pswd == COVID_TASKS_PSWD:
            if task == 'download_and_update_covid':
                print('download and update')
                service.download_and_update_covid()
                ctx = {'status': 'download and update completed'}
            if task == 'download_covid_data_json_notify':
                print('download')
                service.download_covid_data_json_notify()
                ctx = {'status': 'download completed'}
            if task == 'delete_all_countries':
                print('deleted all countries')
                service.delete_all_countries()
                ctx = {'status': 'all countries deleted'}
            if task == 'update_status_notify':
                print('update')
                service.update_status_notify()
                ctx = {'status': 'update completed'}
            if task == 'start background task: update':
                print('task update started')
                status = tasks.task_download_and_update_covid()
                ctx = {'status': status}
        else:
            print('login or password incorrect')
    context = {**service_covid.get_covid_tasks(), **ctx}
    return render(request, 'owid/tasks_owid.html', context)


def covid(request):
    context = service_covid.get_covid_selection_data()
    return render(request, 'owid/covid.html', context)


def numbers(request):
    day = ''
    if request.method == "POST":
        day = request.POST['day']
    print('day = ' + day)
    if day == '':
        day = '0';
    context = service_covid.get_covid_numbers_data(day)
    return render(request, 'owid/numbers.html', context)


def numbers_json(request):
    data = {'country': ''}
    if request.method == 'GET':
        country = request.GET.get('country')
        days = request.GET.get('days')
        data_list = service_covid.get_covid_numbers_data_as_dict(country, days)
        if data_list:
            data['country'] = list(data_list)
    return JsonResponse(data, safe=False)


def country_json(request):
    data = {'country': ''}
    if request.method == 'GET':
        country_name = request.GET.get('country').lower()
        print(country_name)
        country_name = country_name \
            .replace('0', ' ') \
            .replace('1', '\'') \
            .replace('2', '(') \
            .replace('3', ')')
        #    if request.method == "POST":
        #        print(request)
        #        country_name = request.POST['country']
        print(country_name)
        data_dict = service_covid.get_country_data_as_dict(country_name)
        if data_dict:
            # print(data_dict)
            data['country'] = data_dict
        else:
            data['country'] = 'no data for ' + country_name
    return JsonResponse(data, safe=False)


def country_json_chart(request):
    data = {'labels': '', 'values': ''}
    if request.method == 'GET':
        type = request.GET.get('type')
        country_name = request.GET.get('country').lower()
        country_name = country_name \
            .replace('0', ' ') \
            .replace('1', '\'') \
            .replace('2', '(') \
            .replace('3', ')')
        print(country_name)
        data_dict = service_covid.get_country_data_for_chart(type, country_name)
        if data_dict:
            data['country'] = data_dict
        else:
            data['country'] = 'no data for ' + country_name
    return JsonResponse(data, safe=False)


def country(request):
    if request.method == "POST":
        location = request.POST['location']
    else:
        location = 'World'
    context = service_covid.get_country_data(location)
    return render(request, 'owid/country.html', context)


def countries(request):
    locations = []
    date_str = ''
    if request.method == "POST":
        date_str = request.POST['datefilter']
        locations = request.POST.getlist('locations')
        if not len(locations):
            locations_str = request.POST['location']
            locations = eval(locations_str)
    else:
        locations.append('World')
    context = service_covid.get_countries_data(locations, date_str)
    return render(request, 'owid/countries.html', context)


def world(request):
    location = 'World'
    context = service_covid.get_country_data(location)
    return render(request, 'owid/country.html', context)


def charts_bar_newcases_world(request):
    location = 'World'
    context = service_covid.get_newcases_all(location)
    return render(request, 'owid/charts_covid_bar.html', context)


# ------------ multiple locations ------------
def charts_newcases_country_group(request):
    locations_str = request.POST['location']
    daterange_str = request.POST['daterange']
    locations_list = eval(locations_str)
    print(daterange_str)
    context = service_covid.get_newcases_all_group(locations_list, daterange_str)
    return render(request, 'owid/charts_covid_line_group.html', context)


def charts_totalcases_country_group(request):
    locations_str = request.POST['location']
    daterange_str = request.POST['daterange']
    print(locations_str)
    locations_list = eval(locations_str)
    print(locations_list)
    context = service_covid.get_totalcases_all_group(locations_list, daterange_str)
    return render(request, 'owid/charts_covid_line_group.html', context)


def charts_newdeaths_country_group(request):
    locations_str = request.POST['location']
    daterange_str = request.POST['daterange']
    print(locations_str)
    locations_list = eval(locations_str)
    print(locations_list)
    context = service_covid.get_newdeaths_all_group(locations_list, daterange_str)
    return render(request, 'owid/charts_covid_line_group.html', context)


def charts_totaldeaths_country_group(request):
    locations_str = request.POST['location']
    daterange_str = request.POST['daterange']
    print(locations_str)
    locations_list = eval(locations_str)
    print(locations_list)
    context = service_covid.get_totaldeaths_all_group(locations_list, daterange_str)
    return render(request, 'owid/charts_covid_line_group.html', context)


# ------------ multiple locations 100 ------------

def charts_newcases100_country_group(request):
    locations_str = request.POST['location']
    daterange_str = request.POST['daterange']
    print(locations_str)
    locations_list = eval(locations_str)
    print(locations_list)
    context = service_covid.get_newcases100_all_group(locations_list, daterange_str)
    return render(request, 'owid/charts_covid_line_group.html', context)


def charts_totalcases100_country_group(request):
    locations_str = request.POST['location']
    daterange_str = request.POST['daterange']
    print(locations_str)
    locations_list = eval(locations_str)
    print(locations_list)
    context = service_covid.get_totalcases100_all_group(locations_list, daterange_str)
    return render(request, 'owid/charts_covid_line_group.html', context)


def charts_newdeaths100_country_group(request):
    locations_str = request.POST['location']
    daterange_str = request.POST['daterange']
    print(locations_str)
    locations_list = eval(locations_str)
    print(locations_list)
    context = service_covid.get_newdeaths100_all_group(locations_list, daterange_str)
    return render(request, 'owid/charts_covid_line_group.html', context)


def charts_totaldeaths100_country_group(request):
    locations_str = request.POST['location']
    daterange_str = request.POST['daterange']
    print(locations_str)
    locations_list = eval(locations_str)
    print(locations_list)
    context = service_covid.get_totaldeaths100_all_group(locations_list, daterange_str)
    return render(request, 'owid/charts_covid_line_group.html', context)


# ------------ single location ---------------
def charts_bar_newcases_country(request):
    per100 = request.POST['per100']
    location = request.POST['location']
    locations = service_covid.get_location_list()
    if location not in locations:
        return render(request, 'owid/covid.html', {
            'locations': locations,
            'error_message': "You didn't select a country."})
    else:
        context = service_covid.get_newcases_all(location, per100)
        return render(request, 'owid/charts_covid_bar.html', context)


def charts_line_totalcases_country(request):
    per100 = request.POST['per100']
    location = request.POST['location']
    locations = service_covid.get_location_list()
    if location not in locations:
        return render(request, 'owid/covid.html', {
            'locations': locations,
            'error_message': "You didn't select a country."})
    else:
        context = service_covid.get_totalcases_all(location, per100)
        return render(request, 'owid/charts_covid_line.html', context)


def charts_bar_newdeaths_country(request):
    per100 = request.POST['per100']
    location = request.POST['location']
    locations = service_covid.get_location_list()
    if location not in locations:
        return render(request, 'owid/covid.html', {
            'locations': locations,
            'error_message': "You didn't select a country."})
    else:
        context = service_covid.get_newdeaths_all(location, per100)
        return render(request, 'owid/charts_covid_bar.html', context)


def charts_line_totaldeaths_country(request):
    per100 = request.POST['per100']
    location = request.POST['location']
    locations = service_covid.get_location_list()
    if location not in locations:
        return render(request, 'owid/covid.html', {
            'locations': locations,
            'error_message': "You didn't select a country."})
    else:
        context = service_covid.get_totaldeaths_all(location, per100)
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
