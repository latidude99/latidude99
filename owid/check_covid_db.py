import json
import smtplib
from socket import gaierror
from datetime import *

import pytz
from json2html import *

from owid.text_owid import *
from owid.models import *
from main.secrets import *


def read_json_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

# not used at the moment
def isUpdated(data_dict):
    last_json_date = data_dict[OWID_COVID_JSON_CHECK_COUNTRY_CODE]['data'][-1]['date']
    last_json_date_obj = datetime.datetime.strptime(last_json_date, '%Y-%m-%d').date()
    country_obj = Country.objects.using('owid').get(location=OWID_COVID_DB_CHECK_COUNTRY)
    covid_data_objects = country_obj.coviddata_set.all()
    last_db_date = str(covid_data_objects[len(covid_data_objects) - 1].date)
    last_db_date_obj = datetime.datetime.strptime(last_db_date[:10], '%Y-%m-%d').date()
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
        last_db_date_obj = datetime.datetime.strptime(last_db_date[:10], '%Y-%m-%d').date()
    else:
        last_db_date_obj = datetime.datetime.strptime('1950-01-01', '%Y-%m-%d').date()
    last_json_date = data_dict['USA']['data'][-1]['date']
    last_json_date_obj = datetime.datetime.strptime(last_json_date, '%Y-%m-%d').date()
    delta = last_json_date_obj - last_db_date_obj

    if delta.days < 1:
        print('No new data')
        status['messages'].append('No new data')
    else:
        status['messages'].append('New data present')
        import_date = datetime.datetime.now(pytz.timezone('Europe/London'))
        fmt = '%Y-%m-%d %H:%M:%S %Z%z'
        status['update'].append('import date: ' + import_date.strftime(fmt))
        print('New data present. Imported on: ' +  status['update'][0])
        countries = Country.objects.using('owid').all()
        countries_name = [x.location for x in countries]
        for k, v in data_dict.items():
            location = v['location']
            # check if country record is already in db
            # and if not add country to the db
            if location not in countries_name:
                status['update'].append('new country: ' + location)
                print('adding new country: ' + location)
                if 'location' not in v:
                    location = '-1'
                else:
                    location = v['location']
                if 'continent' not in v:
                    continent = '-1'
                else:
                    continent = v['continent']
                if 'population' not in v:
                    population = -1
                else:
                    population = v['population']
                if 'population_density' not in v:
                    population_density = -1
                else:
                    population_density = v['population_density']
                if 'median_age' not in v:
                    median_age = -1
                else:
                    median_age = v['median_age']
                if 'aged_65_older' not in v:
                    aged_65_older = -1
                else:
                    aged_65_older = v['aged_65_older']
                if 'aged_70_older' not in v:
                    aged_70_older = -1
                else:
                    aged_70_older = v['aged_70_older']
                if 'gdp_per_capita' not in v:
                    gdp_per_capita = -1
                else:
                    gdp_per_capita = v['gdp_per_capita']
                if 'cardiovasc_death_rate' not in v:
                    cardiovasc_death_rate = -1
                else:
                    cardiovasc_death_rate = v['cardiovasc_death_rate']
                if 'diabetes_prevalence' not in v:
                    diabetes_prevalence = -1
                else:
                    diabetes_prevalence = v['diabetes_prevalence']
                if 'handwashing_facilities' not in v:
                    handwashing_facilities = -1
                else:
                    handwashing_facilities = v['handwashing_facilities']
                if 'hospital_beds_per_thousand' not in v:
                    hospital_beds_per_thousand = -1
                else:
                    hospital_beds_per_thousand = v['hospital_beds_per_thousand']
                if 'life_expectancy' not in v:
                    life_expectancy = -1
                else:
                    life_expectancy = v['life_expectancy']
                if 'human_development_index' not in v:
                    human_development_index = -1
                else:
                    human_development_index = v['human_development_index']
                country = Country(
                                location=location,
                                continent=continent,
                                population=population,
                                population_density=population_density,
                                median_age=median_age,
                                aged_65_older=aged_65_older,
                                aged_70_older=aged_70_older,
                                gdp_per_capita=gdp_per_capita,
                                cardiovasc_death_rate=cardiovasc_death_rate,
                                diabetes_prevalence=diabetes_prevalence,
                                handwashing_facilities=handwashing_facilities,
                                hospital_beds_per_thousand=hospital_beds_per_thousand,
                                life_expectancy=life_expectancy,
                                human_development_index=human_development_index)
                country.save(using='owid')

            db_country = Country.objects.using('owid').get(location=location)

            covid_data_objects = db_country.coviddata_set.all()
            dates_str = [datetime.datetime.strftime(x.date, '%Y-%m-%d') for x in covid_data_objects]
            #print(dates_str)

            has_new_data = False
            for v1 in v['data']:
             #   data_date_obj = datetime.datetime.strptime(v1['date'], '%Y-%m-%d').date()
             #   delta_country = data_date_obj - last_db_date_obj
                if v1['date'] not in dates_str:
                    print('new data for: ' +db_country.location + ' date: ' + v1['date'])
                    status['update'].append('new data for: ' +db_country.location + ' date: ' + v1['date'])

                    has_new_data = True
                    if 'date' not in v1:
                        date = -1
                    else:
                        date=v1['date'] + ' 00:00:00+00:00'
                    if 'new_cases' not in v1:
                        new_cases = -1
                    else:
                        new_cases=v1['new_cases']
                    if 'total_cases' not in v1:
                        total_cases = -1
                    else:
                        total_cases=v1['total_cases']
                    if 'new_deaths' not in v1:
                        new_deaths = -1
                    else:
                        new_deaths=v1['new_deaths']
                    if 'total_deaths' not in v1:
                        total_deaths = -1
                    else:
                        total_deaths=v1['total_deaths']
                    if 'new_cases_per_million' not in v1:
                        new_cases_per_million = -1
                    else:
                        new_cases_per_million=v1['new_cases_per_million']
                    if 'total_cases_per_million' not in v1:
                        total_cases_per_million = -1
                    else:
                        total_cases_per_million=v1['total_cases_per_million']
                    if 'new_deaths_per_million' not in v1:
                        new_deaths_per_million = -1
                    else:
                        new_deaths_per_million=v1['new_deaths_per_million']
                    if 'total_deaths_per_million' not in v1:
                        total_deaths_per_million = -1
                    else:
                        total_deaths_per_million=v1['total_deaths_per_million']
                    import_date=import_date
                    db_country.coviddata_set.create(date=date,
                                                 new_cases=new_cases,
                                                 total_cases=total_cases,
                                                 new_deaths=new_deaths,
                                                 total_deaths=total_deaths,
                                                 new_cases_per_million=new_cases_per_million,
                                                 total_cases_per_million=total_cases_per_million,
                                                 new_deaths_per_million=new_deaths_per_million,
                                                 total_deaths_per_million=total_deaths_per_million,
                                                 import_date=import_date)

            if has_new_data:
                db_country.save(using='owid')

    return json2html.convert(json = json.dumps(status, indent = 4))


