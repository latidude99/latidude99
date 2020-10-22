from owid.models import *
import datetime




def find_country_coviddata_all(country, daterange_list):
    country_obj = Country.objects.using('owid').get(location=country)
    if len(daterange_list) == 2:
        start = datetime.datetime.strptime(daterange_list[0], "%Y-%m-%d")
        end = datetime.datetime.strptime(daterange_list[1], "%Y-%m-%d")
        coviddata = country_obj.coviddata_set.filter(date__range=[daterange_list[0], daterange_list[1]]).order_by('date')
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



