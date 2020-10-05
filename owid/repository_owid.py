from owid.text_owid import *
from owid.models import *



def find_country_coviddata_all(country):
    country_obj = Country.objects.using('owid').get(location=country)
    coviddata = country_obj.coviddata_set.all()
    return coviddata


def find_countries_all():
    country_objs = Country.objects.using('owid').all()
    return country_objs

def find_country(location):
    country_obj = Country.objects.using('owid').get(location=location)
    return country_obj