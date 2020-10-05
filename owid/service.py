import django

django.setup()

from owid.import_covid import *
from owid.check_covid_db import *
from owid.text_owid import *
from main.send_email import *
from owid.repository_owid import *


def update_owid_covid_db():
    status = get_new_json_covid_data(COVID_DATA_FILE_JSON)
    return status


def check_owid_covid_db():
    status = check_db_against_json_covid_data(COVID_DATA_FILE_JSON)
    return status


def update_status_notify():
    status = update_owid_covid_db()
    send(LATITUDE99_LOGIN, LATITUDE99_LOGIN, 'Import json data into OWID DB status', status)


def check_status_notify():
    status = check_owid_covid_db()
    send(LATITUDE99_LOGIN, LATITUDE99_LOGIN, 'Check OWID DB against json data', status)


def delete_country(country):
    country_obj = Country.objects.using('owid').get(location=country)
    country_obj.delete(using='owid')
    print(country + ' deleted')


print('inside service')

#update_status_notify()

#check_status_notify()
#delete_country('United States')



