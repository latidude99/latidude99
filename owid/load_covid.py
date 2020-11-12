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



def load_json_covid_data(filename):
    data_dict = read_json_file(filename)

    status = {}
    status['messages'] = []
    status['update'] = []
    status['errors'] = []
    import_date = dt.datetime.now(pytz.timezone('Europe/London'))
    db_country = ''
    for k, v in data_dict.items():
        if 'location' not in v:
            location = '-1'
        else:
            location = v['location']
            status['update'].append('add new country: ' + location)
            print('add new country: ' + location)
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
        db_country = Country(
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
        db_country.save(using='owid')

        for v1 in v['data']:
            if 'date' not in v1:
                date = -1
            else:
                date = v1['date'] + ' 00:00:00+00:00'
                status['update'].append('add new data for: ' + db_country.location + ', ' + v1['date'])
                print('add new data for: ' + db_country.location + ', ' + v1['date'])
            if 'new_cases' not in v1:
                new_cases = -1
            else:
                new_cases = v1['new_cases']
            if 'total_cases' not in v1:
                total_cases = -1
            else:
                total_cases = v1['total_cases']
            if 'new_deaths' not in v1:
                new_deaths = -1
            else:
                new_deaths = v1['new_deaths']
            if 'total_deaths' not in v1:
                total_deaths = -1
            else:
                total_deaths = v1['total_deaths']
            if 'new_cases_per_million' not in v1:
                new_cases_per_million = -1
            else:
                new_cases_per_million = v1['new_cases_per_million']
            if 'total_cases_per_million' not in v1:
                total_cases_per_million = -1
            else:
                total_cases_per_million = v1['total_cases_per_million']
            if 'new_deaths_per_million' not in v1:
                new_deaths_per_million = -1
            else:
                new_deaths_per_million = v1['new_deaths_per_million']
            if 'total_deaths_per_million' not in v1:
                total_deaths_per_million = -1
            else:
                total_deaths_per_million = v1['total_deaths_per_million']
            if 'new_cases_smoothed' not in v1:
                new_cases_smoothed = -1
            else:
                new_cases_smoothed = v1['new_cases_smoothed']
            if 'new_deaths_smoothed' not in v1:
                new_deaths_smoothed = -1
            else:
                new_deaths_smoothed = v1['new_deaths_smoothed']
            if 'new_tests' not in v1:
                new_tests = -1
            else:
                new_tests = v1['new_tests']
            if 'total_tests' not in v1:
                total_tests = -1
            else:
                total_tests = v1['total_tests']
            if 'new_tests_smoothed' not in v1:
                new_tests_smoothed = -1
            else:
                new_tests_smoothed = v1['new_tests_smoothed']
            if 'new_cases_smoothed_per_million' not in v1:
                new_cases_smoothed_per_million = -1
            else:
                new_cases_smoothed_per_million = v1['new_cases_smoothed_per_million']
            if 'new_deaths_smoothed_per_million' not in v1:
                new_deaths_smoothed_per_million = -1
            else:
                new_deaths_smoothed_per_million = v1['new_deaths_smoothed_per_million']

            import_date = import_date
            db_country.coviddata_set.create(date=date,
                                            new_cases=new_cases,
                                            total_cases=total_cases,
                                            new_deaths=new_deaths,
                                            total_deaths=total_deaths,
                                            new_cases_per_million=new_cases_per_million,
                                            total_cases_per_million=total_cases_per_million,
                                            new_deaths_per_million=new_deaths_per_million,
                                            total_deaths_per_million=total_deaths_per_million,
                                            new_cases_smoothed=new_cases_smoothed,
                                            new_deaths_smoothed=new_deaths_smoothed,
                                            new_tests=new_tests,
                                            total_tests=total_tests,
                                            new_tests_smoothed=new_tests_smoothed,
                                            new_cases_smoothed_per_million=new_cases_smoothed_per_million,
                                            new_deaths_smoothed_per_million=new_deaths_smoothed_per_million,
                                            import_date=import_date)

            db_country.save(using='owid')

    return json2html.convert(json=json.dumps(status, indent=4))
