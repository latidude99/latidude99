# import django
#
# django.setup()

from owid.models import *
import datetime as dt
import pytz


def find_country_coviddata_all(country, daterange_list):
    country_obj = Country.objects.using('owid').get(location=country)
    if len(daterange_list) == 2:
        start = dt.datetime.strptime(daterange_list[0], "%Y-%m-%d")
        end = dt.datetime.strptime(daterange_list[1], "%Y-%m-%d")
        coviddata = country_obj.coviddata_set.filter(date__range=[daterange_list[0], daterange_list[1]]).order_by(
            'date')
        print('repo: --> ' + daterange_list[0] + ', ' + daterange_list[1])
    else:
        coviddata = country_obj.coviddata_set.all()
    return coviddata


def find_countries_all():
    country_objs = Country.objects.using('owid').all()
    return country_objs


def find_country(location):
    country_obj = Country.objects.using('owid').get(location=location)
    return country_obj


def find_data_by_continent_and_date(continent, date):
    data = []
    covid_data = CovidData.objects.using('owid').filter(country__continent=continent, date=date)
    print(continent)
    data.append(continent.lower().replace(' ', '_'))
    data.append(sum([x.new_cases for x in covid_data]))
    data.append(sum([x.total_cases for x in covid_data]))
    data.append(sum([x.new_deaths for x in covid_data]))
    data.append(sum([x.total_deaths for x in covid_data]))
    return data


def find_data_by_country_continent_latest(date):
    continents = ['Europe', 'Asia', 'Africa', 'North America', 'South America', 'Oceania']
    countries = []
    for cont in continents:
        covid_data = CovidData.objects.using('owid').filter(country__continent=cont, date=date)
        for item in covid_data:
            country = []
            country.append(cont)
            country.append(item.country)
            country.append(item.new_cases)
            country.append(item.total_cases)
            country.append(item.new_deaths)
            country.append(item.total_deaths)
            country.append(item.new_cases_per_million)
            country.append(item.total_cases_per_million)
            country.append(item.new_deaths_per_million)
            country.append(item.total_deaths_per_million)
            country.append(item.country.location
                           .replace("\'", '1')
                           .replace(' ', '0')
                           .replace('(', '2')
                           .replace(')', '3'))
            countries.append(country)
    return countries


def find_data_by_country_latest(country, date):
    countries = []
    covid_data = CovidData.objects.using('owid').filter(country__location=country, date=date).values()
    # for item in covid_data:
    #     country = []
    #     country.append(item.country.continent)
    #     country.append(item.country.location)
    #     country.append(item.new_cases)
    #     country.append(item.total_cases)
    #     country.append(item.new_deaths)
    #     country.append(item.total_deaths)
    #     country.append(item.new_cases_per_million)
    #     country.append(item.total_cases_per_million)
    #     country.append(item.new_deaths_per_million)
    #     country.append(item.total_deaths_per_million)
    #     country.append(item.country.location
    #                    .replace("\'", '1')
    #                    .replace(' ', '0')
    #                    .replace('(', '2')
    #                    .replace(')', '3'))
    #     country.append(item.country.population)
    #     countries.append(country)
    return covid_data





# daterange_list = []
# data_world = find_country_coviddata_all('World', daterange_list)
# date_world = data_world[len(data_world) - 1].date
# print(find_data_by_country_latest('Poland', date_world - dt.timedelta(days=2)))

# daterange_list = []
# data_world = find_country_coviddata_all('World', daterange_list)
# data_world = data_world[len(data_world) - 1]
# covid_data = CovidData.objects.using('owid').filter(country__continent='Europe', date=data_world.date)
# countries = []

# for item in covid_data:
#    country = []
#    country.append(item.country)
#    country.append(item.new_cases)
#    country.append(item.total_cases)
#    country.append(item.new_deaths)
#    country.append(item.total_deaths)
#    country.append(item.new_cases_per_million)
#    country.append(item.total_cases_per_million)
#    country.append(item.new_deaths_per_million)
#    country.append(item.total_deaths_per_million)
#    countries.append(country)

# print(countries[15][1])
