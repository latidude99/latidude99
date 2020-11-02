import json

import datetime as dt

import pytz
from json2html import *

from owid.models import *
from owid.text_owid import *


def read_json_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


# not used at the moment
def isUpdated(data_dict):
    last_json_date = data_dict[OWID_COVID_JSON_CHECK_COUNTRY_CODE]['data'][-1]['date']
    last_json_date_obj = dt.datetime.strptime(last_json_date, '%Y-%m-%d').date()
    country_obj = Country.objects.using('owid').get(location=OWID_COVID_DB_CHECK_COUNTRY)
    covid_data_objects = country_obj.coviddata_set.all()
    last_db_date = str(covid_data_objects[len(covid_data_objects) - 1].date)
    last_db_date_obj = dt.datetime.strptime(last_db_date[:10], '%Y-%m-%d').date()
    delta = last_json_date_obj - last_db_date_obj
    if delta.days > 0:
        return True
    else:
        return False


def check_db_against_json_covid_data(filename):
    data_dict = read_json_file(filename)

    status = {}
    status['messages'] = []
    status['update'] = []
    status['errors'] = []
    db_models_exists = False
    try:
        Country.objects.using('owid').get(location=OWID_COVID_DB_CHECK_COUNTRY)
        db_models_exists = True
    except:
        status['errors'].append('Country.DoesNotExist')
    if db_models_exists is True:
        country_obj = Country.objects.using('owid').get(location=OWID_COVID_DB_CHECK_COUNTRY)
        covid_data_objects = country_obj.coviddata_set.all()
        last_db_date = str(covid_data_objects[len(covid_data_objects) - 1].date)
        last_db_date_obj = dt.datetime.strptime(last_db_date[:10], '%Y-%m-%d').date()
    else:
        last_db_date_obj = dt.datetime.strptime('1950-01-01', '%Y-%m-%d').date()
    last_json_date = data_dict['USA']['data'][-1]['date']
    last_json_date_obj = dt.datetime.strptime(last_json_date, '%Y-%m-%d').date()
    delta = last_json_date_obj - last_db_date_obj

    if delta.days < 1:
        print('No new data')
        status['messages'].append('No new data')
    else:
        status['messages'].append('New data present')
        import_date = dt.datetime.now(pytz.timezone('Europe/London'))
        fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        status['update'].append('import date: ' + import_date.strftime(fmt))
        print('New data present. Imported on: ' + status['update'][0])
        countries = Country.objects.using('owid').all()
        countries_name = [x.location for x in countries]
        for k, v in data_dict.items():
            location = v['location']
            # check if country record is already in db
            # and if not add country to the db
            if location not in countries_name:
                status['update'].append('add new country: ' + location)
                print('adding new country: ' + location)
                continue
            else:
                db_country = Country.objects.using('owid').get(location=location)

                covid_data_objects = db_country.coviddata_set.all()
                dates_str = [dt.datetime.strftime(x.date, '%Y-%m-%d') for x in covid_data_objects]
                # print(dates_str)

                for v1 in v['data']:
                    data_date_obj = dt.datetime.strptime(v1['date'], '%Y-%m-%d').date()
                    delta_country = data_date_obj - last_db_date_obj + dt.timedelta(14)
                    print('delta: ' + str(delta_country.days))
                    if delta_country.days > 0:  # data in json are corrected for past records, looks like about 14 days
                        print('adding data for: ' + db_country.location + ', ' + data_date_obj.strftime('%Y-%m-%d'))
                        status['update'].append('new data for: ' + db_country.location + ', ' + v1['date'])

    return json2html.convert(json=json.dumps(status, indent=4))
