#import django
#django.setup()

from owid.import_covid import *
from owid.check_covid_db import *
from main.send_email import *
from owid.repository_owid import *
import shutil
import urllib
import urllib.request
from latidude99.settings import OWID_DATA_FOLDER
import datetime as dt
import time


def update_owid_covid_db():
    status = get_new_json_covid_data(OWID_DATA_FOLDER + COVID_COVID_DATA_JSON_FILE)
    return status


def check_owid_covid_db():
    status = check_db_against_json_covid_data(OWID_DATA_FOLDER + COVID_COVID_DATA_JSON_FILE)
    return status

def download_covid_data_json_notify():
    url = COVID_COVID_DATA_JSON_URL
    file_path = OWID_DATA_FOLDER + COVID_COVID_DATA_JSON_FILE
    with urllib.request.urlopen(url) as response, open(file_path, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    status = 'JSON file downloaded successfully. File location: ' + file_path
    print(status)
#    send(LATITUDE99_LOGIN, LATITUDE99_LOGIN, 'Download json data status', status)
    print('download finished')


def update_status_notify():
    print('inside service, update, start')
    status = update_owid_covid_db()
 #   send(LATITUDE99_LOGIN, LATITUDE99_LOGIN, 'Import json data into OWID DB status', status)
    print('inside service, update, end')
    return status


def check_status_notify():
    print('inside service, check, start')
    status = check_owid_covid_db()
#    send(LATITUDE99_LOGIN, LATITUDE99_LOGIN, 'Check OWID DB against json data', status)
    print('inside service, check, end')


def delete_country(country):
    country_obj = Country.objects.using('owid').get(location=country)
    country_obj.delete(using='owid')
    print(country + ' deleted')


def download_and_update_covid():
    download_covid_data_json_notify()
    time.sleep(10)
    status = update_status_notify()
    return status



def task_test():
    print(dt.datetime.now())
    print('test back task')





print('inside service')#

#update_status_notify()

#check_status_notify()

#delete_country('Solomon Islands')



