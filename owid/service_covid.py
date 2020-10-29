# import django
# django.setup()

from owid.owid_country_dto import OwidCountryDTO
from owid.text_owid import *
from owid.repository_owid import *
from latidude99.settings import OWID_DATA_FOLDER, OWID_LOG_FOLDER
import datetime as dt
import pytz
import sys

# import pytz

urls_pl_bar = {'newcases': 'charts_pl_newcases_bar',
               'totalcases': 'charts_pl_totalcases_bar',
               'newdeaths': 'charts_pl_newdeaths_bar',
               'totaldeaths': 'charts_pl_totaldeaths_bar'}

LOG_FILE = OWID_LOG_FOLDER + 'log_owid_covid.log'


def log_to_file(file_name, message):
    ORIGINAL_STDOUT = sys.stdout
    with open(file_name, 'a') as f:
        sys.stdout = f
        print(dt.datetime.now())
        print(message)
        print('------------------------')
        sys.stdout = ORIGINAL_STDOUT


def get_covid_tasks():
    context = {'style_css': STYLE_OWID,
               'loader_css': LOADER_CSS,
               'background_pattern1': BACKGROUND_PATTERN1,
               'background_pattern2': BACKGROUND_PATTERN2,
               'background_pattern3': BACKGROUND_PATTERN3,
               'background_pattern4': BACKGROUND_PATTERN4,
               'background_pattern5': BACKGROUND_PATTERN5,
               'latidude99': 'latidude99.com',
               'title': OWID_COVID_TITLE.title,
               'subtitle': OWID_COVID_SUBTITLE,
               'data_supply': OWID_DATA_SUPPLY,
               'image_globe': IMAGE_GLOBE,
               'image_coronavirus': IMAGE_CORONAVIRUS,
               }
    return context


def get_location_list():
    country_objs = find_countries_all()
    locations = [x.location for x in country_objs]
    locations.sort()
    return locations


def get_data_for_location(location):
    country = find_country(location)
    return country


def get_covid_selection_data():
    daterange_list = []
    locations = get_location_list()
    data_world = find_country_coviddata_all('World', daterange_list)
    data_world = data_world[len(data_world) - 1]
    date = data_world.date.strftime("%A, %d %B %Y")
    data_rest = []
    data_rest.append(find_data_by_continent_and_date('Europe', data_world.date))
    data_rest.append(find_data_by_continent_and_date('Asia', data_world.date))
    data_rest.append(find_data_by_continent_and_date('Africa', data_world.date))
    data_rest.append(find_data_by_continent_and_date('North America', data_world.date))
    data_rest.append(find_data_by_continent_and_date('South America', data_world.date))
    data_rest.append(find_data_by_continent_and_date('Oceania', data_world.date))
    context = {'the_world': THE_WORLD,
               'europe': EUROPE,
               'asia': ASIA,
               'africa': AFRICA,
               'north_america': NORTH_AM,
               'south_america': SOUTH_AM,
               'oceania': OCEANIA,
               'see_all_countries': SEE_ALL_BTN,
               'style_css': STYLE_OWID,
               'background_pattern1': BACKGROUND_PATTERN1,
               'background_pattern2': BACKGROUND_PATTERN2,
               'background_pattern3': BACKGROUND_PATTERN3,
               'background_pattern4': BACKGROUND_PATTERN4,
               'background_pattern5': BACKGROUND_PATTERN5,
               'latidude99': 'latidude99.com',
               'title': OWID_COVID_TITLE.title,
               'subtitle': OWID_COVID_SUBTITLE,
               'locations': locations,
               'data_supply': OWID_DATA_SUPPLY,
               'image_globe': IMAGE_GLOBE,
               'image_coronavirus': IMAGE_CORONAVIRUS,
               'select_locations': SELECT_LOCATIONS,
               'select_locations_sub': SELECT_LOCATIONS_SUB,
               'country_card_title': COUNTRY_CARD_TITLE,
               'btn_country': BTN_COUNTRY,
               'btn_countries': BTN_COUNTRIES,
               'new_cases': NEW_CASES_TXT,
               'total_cases': TOTAL_CASES_TXT,
               'new_deaths': NEW_DEATHS_TXT,
               'total_deaths': TOTAL_DEATHS_TXT,
               'info': COVID_INFO,
               'data_world': data_world,
               'date': date,
               'data_rest': data_rest,
               'loader_css': LOADER_CSS,
               }
    return context


data_latest_all = ['', []]

def get_covid_numbers_data():
    daterange_list = []
    data_world = find_country_coviddata_all('World', daterange_list)
    data_world = data_world[len(data_world) - 1]
    date = data_world.date.strftime("%A, %d %B %Y")
    last_db_date = data_world.date
    current_date = dt.datetime.utcnow().replace(tzinfo=pytz.UTC)
    delta = current_date - last_db_date
    print(delta)
    if data_latest_all[0] != '' and delta.days > 0 and data_latest_all[1]:
        data = data_latest_all[1]
        print('if')
    else:
        data = find_data_by_country_latest(data_world.date)
        data_latest_all[0] = data_world.date
        data_latest_all[1] = data
        print('else')
    print(data[15][1].population)
    context = {'date': date,
               'data': data,
               'the_world': THE_WORLD,
               'europe': EUROPE,
               'asia': ASIA,
               'africa': AFRICA,
               'north_america': NORTH_AM,
               'south_america': SOUTH_AM,
               'oceania': OCEANIA,
               'style_css': STYLE_OWID,
               'loader_css': LOADER_CSS,
               'tablesorter_js': TABLESORTER_JS,
               'background_pattern1': BACKGROUND_PATTERN1,
               'background_pattern2': BACKGROUND_PATTERN2,
               'background_pattern3': BACKGROUND_PATTERN3,
               'background_pattern4': BACKGROUND_PATTERN4,
               'background_pattern5': BACKGROUND_PATTERN5,
               'image_coronavirus': IMAGE_CORONAVIRUS,
               'btn_country': BTN_COUNTRY_CHANGE,
               'side_txt1': SIDE_TXT_1,
               'milky_way': MILKY_WAY,
               'latidude99': 'latidude99.com',
               'no_data': NO_DATA,
               'ppl': PPL,
               'per_1_million': PER_1_MILLION,
               'per_100_000': PER_100_000,
               'per_1000': PER_1000,
               'country_name': COUNTRY_NAME,
               'continent': CONTINENT,
               'population': POPULATION,
               'new_cases': NEW_CASES_TXT,
               'total_cases': TOTAL_CASES_TXT,
               'new_deaths': NEW_DEATHS_TXT,
               'total_deaths': TOTAL_DEATHS_TXT,
               'btn_charts': BTN_CHARTS_TXT,
               'new_cases100': NEW_CASES_TXT100,
               'total_cases100': TOTAL_CASES_TXT100,
               'new_deaths100': NEW_DEATHS_TXT100,
               'total_deaths100': TOTAL_DEATHS_TXT100,
               }
    return context


def get_country_data(location):
    daterange_list = []
    locations = get_location_list()
    location_flag = 'flags_small/' + location.lower().replace(' ', '-') + '.png'
    country = find_country(location)
    data = find_country_coviddata_all(location, daterange_list)
    context = {'footer_info': FOOTER_INFO,
               'style_css': STYLE_OWID,
               'background_pattern1': BACKGROUND_PATTERN1,
               'background_pattern2': BACKGROUND_PATTERN2,
               'background_pattern3': BACKGROUND_PATTERN3,
               'background_pattern4': BACKGROUND_PATTERN4,
               'background_pattern5': BACKGROUND_PATTERN5,
               'image_coronavirus': IMAGE_CORONAVIRUS,
               'btn_country': BTN_COUNTRY_CHANGE,
               'locations': locations,
               'flag': location_flag,
               'side_txt1': SIDE_TXT_1,
               'milky_way': MILKY_WAY,
               'latidude99': 'latidude99.com',
               'no_data': NO_DATA,
               'millions': MILLIONS,
               'years': YEARS,
               'ppl': PPL,
               'km': KM,
               'sq': SQ,
               'per_100_000': PER_100_000,
               'per_1000': PER_1000,
               'percent': PERCENT,
               'dollars': DOLLARS,
               'location': location,
               'country': country,
               'data': data,
               'continent': CONTINENT,
               'population': POPULATION,
               'population_density': POPULATION_DENSITY,
               'median_age': MEDIAN_AGE,
               'aged_65_older': AGED_65_OLDER,
               'aged_70_older': AGED_70_OLDER,
               'gdp_per_capita': GDP_PER_CAPITA,
               'cardiovasc_death_rate': CARDIOVASC_DEATH_RATE,
               'diabetes_prevalence': DIABETES_PREVALENCE,
               'handwashing_facilities': HANDWASHING_FACILITIES,
               'hospital_beds_per_thousand': HOSPITAL_BEDS_PER_THOUSAND,
               'life_expectancy': LIFE_EXPECTANCY,
               'human_development_index': HUMAN_DEVELOPMENT_INDEX,
               'population_desc': POPULATION_DESC,
               'population_density_desc': POPULATION_DENSITY_DESC,
               'median_age_desc': MEDIAN_AGE_DESC,
               'aged_65_older_desc': AGED_65_OLDER_DESC,
               'aged_70_older_desc': AGED_70_OLDER_DESC,
               'gdp_per_capita_desc': GDP_PER_CAPITA_DESC,
               'cardiovasc_death_rate_desc': CARDIOVASC_DEATH_RATE_DESC,
               'diabetes_prevalence_desc': DIABETES_PREVALENCE_DESC,
               'handwashing_facilities_desc': HANDWASHING_FACILITIES_DESC,
               'hospital_beds_per_thousand_desc': HOSPITAL_BEDS_PER_THOUSAND_DESC,
               'life_expectancy_desc': LIFE_EXPECTANCY_DESC,
               'human_development_index_desc': HUMAN_DEVELOPMENT_INDEX_DESC,
               'new_cases': NEW_CASES_TXT,
               'total_cases': TOTAL_CASES_TXT,
               'new_deaths': NEW_DEATHS_TXT,
               'total_deaths': TOTAL_DEATHS_TXT,
               'btn_charts': BTN_CHARTS_TXT,
               'new_cases100': NEW_CASES_TXT100,
               'total_cases100': TOTAL_CASES_TXT100,
               'new_deaths100': NEW_DEATHS_TXT100,
               'total_deaths100': TOTAL_DEATHS_TXT100,
               }
    return context


def get_countries_data(countries_selected, date_str):
    date_list = date_str.split('  to  ')
    if len(date_list) == 1:
        date_list.append('')
    elif len(date_list) == 0:
        date_list = ['', '']
    locations = get_location_list()
    flags = []
    countries = []
    countries_names = []
    #    countries_data = []
    for c in countries_selected:
        flag = 'flags_small/' + c.lower().replace(' ', '-') + '.png'
        flags.append(flag)
        country = find_country(c)
        countries.append(country)
        countries_names.append(c)
    #       data = find_country_coviddata_all(country)
    #       countries_data.append(data)
    print(countries)
    context = {'footer_info': FOOTER_INFO,
               'style_css': STYLE_OWID,
               'background_pattern1': BACKGROUND_PATTERN1,
               'background_pattern2': BACKGROUND_PATTERN2,
               'background_pattern3': BACKGROUND_PATTERN3,
               'background_pattern4': BACKGROUND_PATTERN4,
               'background_pattern5': BACKGROUND_PATTERN5,
               'image_coronavirus': IMAGE_CORONAVIRUS,
               'btn_country': BTN_COUNTRY_CHANGE,
               'btn_countries_reselect': BTN_COUNTRIES_RESELECT,
               'locations': locations,
               'side_txt1': SIDE_TXT_1,
               'milky_way': MILKY_WAY,
               'latidude99': 'latidude99.com',
               'no_data': NO_DATA,
               'millions': MILLIONS,
               'years': YEARS,
               'ppl': PPL,
               'km': KM,
               'sq': SQ,
               'per_100_000': PER_100_000,
               'per_1000': PER_1000,
               'percent': PERCENT,
               'dollars': DOLLARS,
               # 'location': location,
               'flags': flags,
               'countries': countries,
               'countries_names': countries_names,
               'date_range': date_str,
               'start_date': date_list[0],
               'end_date': date_list[1],
               #  'countries_data': countries_data,
               'continent': CONTINENT,
               'country_name': COUNTRY_NAME,
               'population': POPULATION,
               'population_density': POPULATION_DENSITY,
               'median_age': MEDIAN_AGE,
               'aged_65_older': AGED_65_OLDER,
               'aged_70_older': AGED_70_OLDER,
               'gdp_per_capita': GDP_PER_CAPITA,
               'cardiovasc_death_rate': CARDIOVASC_DEATH_RATE,
               'diabetes_prevalence': DIABETES_PREVALENCE,
               'handwashing_facilities': HANDWASHING_FACILITIES,
               'hospital_beds_per_thousand': HOSPITAL_BEDS_PER_THOUSAND,
               'life_expectancy': LIFE_EXPECTANCY,
               'human_development_index': HUMAN_DEVELOPMENT_INDEX,
               'population_desc': POPULATION_DESC,
               'population_density_desc': POPULATION_DENSITY_DESC,
               'median_age_desc': MEDIAN_AGE_DESC,
               'aged_65_older_desc': AGED_65_OLDER_DESC,
               'aged_70_older_desc': AGED_70_OLDER_DESC,
               'gdp_per_capita_desc': GDP_PER_CAPITA_DESC,
               'cardiovasc_death_rate_desc': CARDIOVASC_DEATH_RATE_DESC,
               'diabetes_prevalence_desc': DIABETES_PREVALENCE_DESC,
               'handwashing_facilities_desc': HANDWASHING_FACILITIES_DESC,
               'hospital_beds_per_thousand_desc': HOSPITAL_BEDS_PER_THOUSAND_DESC,
               'life_expectancy_desc': LIFE_EXPECTANCY_DESC,
               'human_development_index_desc': HUMAN_DEVELOPMENT_INDEX_DESC,
               'new_cases': NEW_CASES_TXT,
               'total_cases': TOTAL_CASES_TXT,
               'new_deaths': NEW_DEATHS_TXT,
               'total_deaths': TOTAL_DEATHS_TXT,
               'btn_charts': BTN_CHARTS_TXT,
               'new_cases100': NEW_CASES_TXT100,
               'total_cases100': TOTAL_CASES_TXT100,
               'new_deaths100': NEW_DEATHS_TXT100,
               'total_deaths100': TOTAL_DEATHS_TXT100,
               }
    return context


# ---------- multiple locations -----------------------


def get_charts_base_context():
    back_colours = ['white', 'yellow', 'red', 'blue', 'green']
    border_colours = ['white', 'yellow', 'red', 'blue', 'green']
    ctx = {'back_btn_selection': CHARTS_BACKTOSELECTION_BTN,
           'dataset_label': CHARTS_LABEL_NEWCASES,
           'back_colours': back_colours,
           'border_colours': border_colours,
           'new_cases': NEW_CASES_TXT,
           'total_cases': TOTAL_CASES_TXT,
           'new_deaths': NEW_DEATHS_TXT,
           'total_deaths': TOTAL_DEATHS_TXT,
           'new_cases100': NEW_CASES_TXT100,
           'total_cases100': TOTAL_CASES_TXT100,
           'new_deaths100': NEW_DEATHS_TXT100,
           'total_deaths100': TOTAL_DEATHS_TXT100,
           }
    return ctx


def get_newcases_all_group(countries_selected, daterange_str):
    daterange_list = daterange_str.split('  to  ')
    flags = []
    countries = []
    countries_names = []
    min_labels = 1000000;
    for c in countries_selected:
        countries_names.append(c)
        flag = 'flags_small/' + c.lower().replace(' ', '-') + '.png'
        flags.append(flag)
        #        country = find_country(c)
        data = find_country_coviddata_all(c, daterange_list)
        no_data = 'NaN'
        values = [x.new_cases if x.new_cases > 0 else no_data for x in data]
        labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in data]
        if len(labels) < min_labels:
            min_labels = len(labels)
        owid_country_dto = OwidCountryDTO(c, c, flag, '0', values, labels)
        countries.append(owid_country_dto)
    for c in countries:
        start = (len(c.labels) - min_labels)
        c.labels = c.labels[start:]
        c.values = c.values[start:]
    context = {'title': TITLE_CHARTS_NEWCASES,
               'flags': flags,
               'countries': countries,
               'countries_names': countries_names,
               'daterange': daterange_str,
               }
    ctx = {**get_covid_selection_data(), **get_charts_base_context(), **context}
    return ctx


def get_totalcases_all_group(countries_selected, daterange_str):
    daterange_list = daterange_str.split('  to  ')
    flags = []
    countries = []
    countries_names = []
    min_labels = 1000000;
    for c in countries_selected:
        countries_names.append(c)
        flag = 'flags_small/' + c.lower().replace(' ', '-') + '.png'
        flags.append(flag)
        #        country = find_country(c)
        data = find_country_coviddata_all(c, daterange_list)
        no_data = 'NaN'
        values = [x.total_cases if x.total_cases > 0 else no_data for x in data]
        labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in data]
        if len(labels) < min_labels:
            min_labels = len(labels)
        owid_country_dto = OwidCountryDTO(c, c, flag, '0', values, labels)
        countries.append(owid_country_dto)
    for c in countries:
        start = (len(c.labels) - min_labels)
        c.labels = c.labels[start:]
        c.values = c.values[start:]
    context = {'title': TITLE_CHARTS_TOTALCASES,
               'flags': flags,
               'countries': countries,
               'countries_names': countries_names,
               'daterange': daterange_str,
               }
    ctx = {**get_covid_selection_data(), **get_charts_base_context(), **context}
    return ctx


def get_newdeaths_all_group(countries_selected, daterange_str):
    daterange_list = daterange_str.split('  to  ')
    flags = []
    countries = []
    countries_names = []
    min_labels = 1000000;
    for c in countries_selected:
        countries_names.append(c)
        flag = 'flags_small/' + c.lower().replace(' ', '-') + '.png'
        flags.append(flag)
        #        country = find_country(c)
        data = find_country_coviddata_all(c, daterange_list)
        no_data = 'NaN'
        values = [x.new_deaths if x.new_deaths > 0 else no_data for x in data]
        labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in data]
        if len(labels) < min_labels:
            min_labels = len(labels)
        owid_country_dto = OwidCountryDTO(c, c, flag, '0', values, labels)
        countries.append(owid_country_dto)
    for c in countries:
        start = (len(c.labels) - min_labels)
        c.labels = c.labels[start:]
        c.values = c.values[start:]
    context = {'title': TITLE_CHARTS_NEWDEATHS,
               'flags': flags,
               'countries': countries,
               'countries_names': countries_names,
               'daterange': daterange_str,
               }
    ctx = {**get_covid_selection_data(), **get_charts_base_context(), **context}
    return ctx


def get_totaldeaths_all_group(countries_selected, daterange_str):
    daterange_list = daterange_str.split('  to  ')
    flags = []
    countries = []
    countries_names = []
    min_labels = 1000000;
    for c in countries_selected:
        countries_names.append(c)
        flag = 'flags_small/' + c.lower().replace(' ', '-') + '.png'
        flags.append(flag)
        #        country = find_country(c)
        data = find_country_coviddata_all(c, daterange_list)
        no_data = 'NaN'
        values = [x.total_deaths if x.total_deaths > 0 else no_data for x in data]
        labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in data]
        if len(labels) < min_labels:
            min_labels = len(labels)
        owid_country_dto = OwidCountryDTO(c, c, flag, '0', values, labels)
        countries.append(owid_country_dto)
    for c in countries:
        start = (len(c.labels) - min_labels)
        c.labels = c.labels[start:]
        c.values = c.values[start:]
    context = {'title': TITLE_CHARTS_TOTALDEATHS,
               'flags': flags,
               'countries': countries,
               'countries_names': countries_names,
               'daterange': daterange_str,
               }
    ctx = {**get_covid_selection_data(), **get_charts_base_context(), **context}
    return ctx


# ---------- multiple locations 100 -----------------------

def get_newcases100_all_group(countries_selected, daterange_str):
    daterange_list = daterange_str.split('  to  ')
    flags = []
    countries = []
    countries_names = []
    min_labels = 1000000;
    for c in countries_selected:
        countries_names.append(c)
        flag = 'flags_small/' + c.lower().replace(' ', '-') + '.png'
        flags.append(flag)
        country = find_country(c)
        per100 = country.population / 100000
        data = find_country_coviddata_all(c, daterange_list)
        no_data = 'NaN'
        values = [x.new_cases / per100 if x.new_cases > 0 else no_data for x in data]
        labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in data]
        if len(labels) < min_labels:
            min_labels = len(labels)
        owid_country_dto = OwidCountryDTO(c, c, flag, '0', values, labels)
        countries.append(owid_country_dto)
    for c in countries:
        start = (len(c.labels) - min_labels)
        c.labels = c.labels[start:]
        c.values = c.values[start:]
    context = {'title': TITLE_CHARTS_NEWCASES100,
               'flags': flags,
               'countries': countries,
               'countries_names': countries_names,
               'daterange': daterange_str,
               }
    ctx = {**get_covid_selection_data(), **get_charts_base_context(), **context}
    return ctx


def get_totalcases100_all_group(countries_selected, daterange_str):
    daterange_list = daterange_str.split('  to  ')
    flags = []
    countries = []
    countries_names = []
    min_labels = 1000000;
    for c in countries_selected:
        countries_names.append(c)
        flag = 'flags_small/' + c.lower().replace(' ', '-') + '.png'
        flags.append(flag)
        country = find_country(c)
        per100 = country.population / 100000
        data = find_country_coviddata_all(c, daterange_list)
        no_data = 'NaN'
        values = [x.total_cases / per100 if x.total_cases > 0 else no_data for x in data]
        labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in data]
        if len(labels) < min_labels:
            min_labels = len(labels)
        owid_country_dto = OwidCountryDTO(c, c, flag, '0', values, labels)
        countries.append(owid_country_dto)
    for c in countries:
        start = (len(c.labels) - min_labels)
        c.labels = c.labels[start:]
        c.values = c.values[start:]
    context = {'title': TITLE_CHARTS_TOTALCASES100,
               'flags': flags,
               'countries': countries,
               'countries_names': countries_names,
               'daterange': daterange_str,
               }
    ctx = {**get_covid_selection_data(), **get_charts_base_context(), **context}
    return ctx


def get_newdeaths100_all_group(countries_selected, daterange_str):
    daterange_list = daterange_str.split('  to  ')
    flags = []
    countries = []
    countries_names = []
    min_labels = 1000000;
    for c in countries_selected:
        countries_names.append(c)
        flag = 'flags_small/' + c.lower().replace(' ', '-') + '.png'
        flags.append(flag)
        country = find_country(c)
        per100 = country.population / 100000
        data = find_country_coviddata_all(c, daterange_list)
        no_data = 'NaN'
        values = [x.new_deaths / per100 if x.new_deaths > 0 else no_data for x in data]
        labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in data]
        if len(labels) < min_labels:
            min_labels = len(labels)
        owid_country_dto = OwidCountryDTO(c, c, flag, '0', values, labels)
        countries.append(owid_country_dto)
    for c in countries:
        start = (len(c.labels) - min_labels)
        c.labels = c.labels[start:]
        c.values = c.values[start:]
    context = {'title': TITLE_CHARTS_NEWDEATHS100,
               'flags': flags,
               'countries': countries,
               'countries_names': countries_names,
               'daterange': daterange_str,
               }
    ctx = {**get_covid_selection_data(), **get_charts_base_context(), **context}
    return ctx


def get_totaldeaths100_all_group(countries_selected, daterange_str):
    daterange_list = daterange_str.split('  to  ')
    flags = []
    countries = []
    countries_names = []
    min_labels = 1000000;
    for c in countries_selected:
        countries_names.append(c)
        flag = 'flags_small/' + c.lower().replace(' ', '-') + '.png'
        flags.append(flag)
        country = find_country(c)
        per100 = country.population / 100000
        data = find_country_coviddata_all(c, daterange_list)
        no_data = 'NaN'
        values = [x.total_deaths / per100 if x.total_deaths > 0 else no_data for x in data]
        labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in data]
        if len(labels) < min_labels:
            min_labels = len(labels)
        owid_country_dto = OwidCountryDTO(c, c, flag, '0', values, labels)
        countries.append(owid_country_dto)
        print('country : ' + c + ', dates: ' + str(len(labels)) + ', values: ' + str(len(values)))
    for c in countries:
        start = (len(c.labels) - min_labels)
        c.labels = c.labels[start:]
        c.values = c.values[start:]
    context = {'title': TITLE_CHARTS_TOTALDEATHS100,
               'flags': flags,
               'countries': countries,
               'countries_names': countries_names,
               'daterange': daterange_str,
               }
    ctx = {**get_covid_selection_data(), **get_charts_base_context(), **context}
    return ctx


# ---------- single location --------------------------


def get_newcases_all(location, per100switch):
    daterange_list = []
    country = find_country(location)
    per100 = country.population / 100000
    location_flag = 'flags_small/' + location.lower().replace(' ', '-') + '.png'
    coviddata = find_country_coviddata_all(location, daterange_list)
    labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in coviddata]
    if per100switch == 'True':
        values = [x.new_cases / per100 if x.new_cases >= 0 else 0 for x in coviddata]
    else:
        values = [x.new_cases if x.new_cases >= 0 else 0 for x in coviddata]
    context = {'location': location,
               'back_btn': CHARTS_BACKTOCOUNTRY_BTN,
               'labels': labels,
               'values': values,
               'dataset_label': CHARTS_LABEL_NEWCASES,
               'back_colour': CHARTS_COVID_CASES_BAR_COLOR_BACK,
               'border_colour': CHARTS_COVID_CASES_BAR_COLOR_BORD,
               'title': 'COVID19, new cases in ' + location[0].capitalize() + location[1:],
               'flag': location_flag,
               'new_cases': NEW_CASES_TXT,
               'total_cases': TOTAL_CASES_TXT,
               'new_deaths': NEW_DEATHS_TXT,
               'total_deaths': TOTAL_DEATHS_TXT,
               'new_cases100': NEW_CASES_TXT100,
               'total_cases100': TOTAL_CASES_TXT100,
               'new_deaths100': NEW_DEATHS_TXT100,
               'total_deaths100': TOTAL_DEATHS_TXT100,
               }
    ctx = {**get_covid_selection_data(), **context}
    return ctx


def get_totalcases_all(location, per100switch):
    daterange_list = []
    country = find_country(location)
    per100 = country.population / 100000
    location_flag = 'flags_small/' + location.lower().replace(' ', '-') + '.png'
    coviddata = find_country_coviddata_all(location, daterange_list)
    labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in coviddata]
    labels = list(dict.fromkeys(labels))
    if per100switch == 'True':
        values = [x.total_cases / per100 if x.total_cases >= 0 else 0 for x in coviddata]
    else:
        values = [x.total_cases if x.total_cases >= 0 else 0 for x in coviddata]
    # values = list(dict.fromkeys(values))
    context = {'location': location,
               'back_btn': CHARTS_BACKTOCOUNTRY_BTN,
               'labels': labels,
               'values': values,
               'dataset_label': CHARTS_LABEL_TOTALCASES,
               'back_colour': CHARTS_COVID_CASES_BAR_COLOR_BACK,
               'border_colour': CHARTS_COVID_CASES_BAR_COLOR_BORD,
               'title': 'COVID19, total cases in ' + location[0].capitalize() + location[1:],
               'flag': location_flag,
               'new_cases': NEW_CASES_TXT,
               'total_cases': TOTAL_CASES_TXT,
               'new_deaths': NEW_DEATHS_TXT,
               'total_deaths': TOTAL_DEATHS_TXT,
               'new_cases100': NEW_CASES_TXT100,
               'total_cases100': TOTAL_CASES_TXT100,
               'new_deaths100': NEW_DEATHS_TXT100,
               'total_deaths100': TOTAL_DEATHS_TXT100,
               }
    ctx = {**get_covid_selection_data(), **context}
    return ctx


def get_newdeaths_all(location, per100switch):
    daterange_list = []
    country = find_country(location)
    per100 = country.population / 100000
    location_flag = 'flags_small/' + location.lower().replace(' ', '-') + '.png'
    coviddata = find_country_coviddata_all(location, daterange_list)
    labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in coviddata]
    labels = list(dict.fromkeys(labels))
    if per100switch == 'True':
        values = [x.new_deaths / per100 if x.new_deaths >= 0 else 0 for x in coviddata]
    else:
        values = [x.new_deaths if x.new_deaths >= 0 else 0 for x in coviddata]
    # values = list(dict.fromkeys(values))
    context = {'location': location,
               'back_btn': CHARTS_BACKTOCOUNTRY_BTN,
               'labels': labels,
               'values': values,
               'dataset_label': CHARTS_LABEL_NEWDEATHS,
               'back_colour': CHARTS_COVID_DEATHS_BAR_COLOR_BACK,
               'border_colour': CHARTS_COVID_DEATHS_BAR_COLOR_BORD,
               'title': 'COVID19, new deaths in ' + location[0].capitalize() + location[1:],
               'flag': location_flag,
               'new_cases': NEW_CASES_TXT,
               'total_cases': TOTAL_CASES_TXT,
               'new_deaths': NEW_DEATHS_TXT,
               'total_deaths': TOTAL_DEATHS_TXT,
               'new_cases100': NEW_CASES_TXT100,
               'total_cases100': TOTAL_CASES_TXT100,
               'new_deaths100': NEW_DEATHS_TXT100,
               'total_deaths100': TOTAL_DEATHS_TXT100,
               }
    ctx = {**get_covid_selection_data(), **context}
    return ctx


def get_totaldeaths_all(location, per100switch):
    daterange_list = []
    country = find_country(location)
    per100 = country.population / 100000
    location_flag = 'flags_small/' + location.lower().replace(' ', '-') + '.png'
    coviddata = find_country_coviddata_all(location, daterange_list)
    labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in coviddata]
    labels = list(dict.fromkeys(labels))
    if per100switch == 'True':
        values = [x.total_deaths / per100 if x.total_deaths >= 0 else 0 for x in coviddata]
    else:
        values = [x.total_deaths if x.total_deaths >= 0 else 0 for x in coviddata]
    # values = list(dict.fromkeys(values))
    context = {'location': location,
               'back_btn': CHARTS_BACKTOCOUNTRY_BTN,
               'labels': labels,
               'values': values,
               'dataset_label': CHARTS_LABEL_TOTALCASES,
               'back_colour': CHARTS_COVID_DEATHS_BAR_COLOR_BACK,
               'border_colour': CHARTS_COVID_DEATHS_BAR_COLOR_BORD,
               'title': 'COVID19, total deaths in ' + location[0].capitalize() + location[1:],
               'flag': location_flag,
               'new_cases': NEW_CASES_TXT,
               'total_cases': TOTAL_CASES_TXT,
               'new_deaths': NEW_DEATHS_TXT,
               'total_deaths': TOTAL_DEATHS_TXT,
               'new_cases100': NEW_CASES_TXT100,
               'total_cases100': TOTAL_CASES_TXT100,
               'new_deaths100': NEW_DEATHS_TXT100,
               'total_deaths100': TOTAL_DEATHS_TXT100,
               }
    ctx = {**get_covid_selection_data(), **context}
    return ctx

    # --------- old -------------


def get_pl_newcases_all():
    pl_coviddata = find_country_coviddata_all('Poland')
    labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in pl_coviddata]
    values = [x.new_cases for x in pl_coviddata]
    context = {'urls_pl_bar': urls_pl_bar,
               'labels': labels,
               'values': values,
               'dataset_label': CHARTS_LABEL_NEWCASES,
               'back_colour': CHARTS_COVID_CASES_BAR_COLOR_BACK,
               'border_colour': CHARTS_COVID_CASES_BAR_COLOR_BORD,
               'title': 'COVID19, new cases in Poland',
               'flag': 'flags/poland_flag_wave_1.png'}
    return context


def get_pl_totalcases_all():
    pl_coviddata = find_country_coviddata_all('Poland')
    labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in pl_coviddata]
    values = [x.total_cases for x in pl_coviddata]
    context = {'urls_pl_bar': urls_pl_bar,
               'labels': labels,
               'values': values,
               'dataset_label': CHARTS_LABEL_TOTALCASES,
               'back_colour': CHARTS_COVID_CASES_BAR_COLOR_BACK,
               'border_colour': CHARTS_COVID_CASES_BAR_COLOR_BORD,
               'title': 'COVID19, total cases in Poland',
               'flag': 'flags/poland_flag_wave_1.png'}
    return context


def get_pl_newdeaths_all():
    pl_coviddata = find_country_coviddata_all('Poland')
    labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in pl_coviddata]
    values = [x.new_deaths for x in pl_coviddata]
    context = {'urls_pl_bar': urls_pl_bar,
               'labels': labels,
               'values': values,
               'dataset_label': CHARTS_LABEL_NEWDEATHS,
               'back_colour': CHARTS_COVID_DEATHS_BAR_COLOR_BACK,
               'border_colour': CHARTS_COVID_DEATHS_BAR_COLOR_BORD,
               'title': 'COVID19, new deaths in Poland',
               'flag': 'flags/poland_flag_wave_1.png'}
    return context


def get_pl_totaldeaths_all():
    pl_coviddata = find_country_coviddata_all('Poland')
    labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in pl_coviddata]
    values = [x.total_deaths for x in pl_coviddata]
    context = {'urls_pl_bar': urls_pl_bar,
               'labels': labels,
               'values': values,
               'dataset_label': CHARTS_LABEL_TOTALDEATHS,
               'back_colour': CHARTS_COVID_DEATHS_BAR_COLOR_BACK,
               'border_colour': CHARTS_COVID_DEATHS_BAR_COLOR_BORD,
               'title': 'COVID19, total deaths in Poland',
               'flag': 'flags/poland_flag_wave_1.png'}
    return context
