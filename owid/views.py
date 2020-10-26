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
            if task == 'download_covid_data_json_notify':
                print('download')
                service.download_covid_data_json_notify()
                ctx = {'status': 'download completed'}
            if task == 'check_status_notify':
                print('check')
                service.check_status_notify()
                ctx = {'status': 'check completed'}
            if task == 'update_status_notify':
                print('update')
                service.update_status_notify()
                ctx = {'status': 'update completed'}
            if task == 'start background task: update':
                print('task update started')
                tasks.back_task_1(repeat=10, repeat_until=None)
                ctx = {'status': 'task update started'}
        else:
            print('login or password incorrect')
    context = {**service_covid.get_covid_tasks(), **ctx}
    return render(request, 'owid/tasks_owid.html', context)


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


