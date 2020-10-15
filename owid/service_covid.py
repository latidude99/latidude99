import django

django.setup()

from owid.import_covid import *
from owid.text_owid import *
from main.send_email import *
from owid.repository_owid import *

urls_pl_bar = {'newcases': 'charts_pl_newcases_bar',
               'totalcases': 'charts_pl_totalcases_bar',
               'newdeaths': 'charts_pl_newdeaths_bar',
               'totaldeaths': 'charts_pl_totaldeaths_bar'}


def get_location_list():
    country_objs = find_countries_all()
    locations = [x.location for x in country_objs]
    locations.sort()
    return locations


def get_data_for_location(location):
    country = find_country(location)
    return country


def get_covid_selection_data():
    locations = get_location_list()
    context = {'footer_info': FOOTER_INFO,
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
               'btn_country': BTN_COUNTRY}
    return context


def get_country_data(location):
    locations = get_location_list()
    location_flag = 'flags_small/' + location.lower().replace(' ', '-') + '.png'
    country = find_country(location)
    data = find_country_coviddata_all(location)
    context = {'footer_info': FOOTER_INFO,
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
               'no_data':NO_DATA,
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
               'btn_charts': BTN_CHARTS_TXT
               }
    return context


def get_newcases_all(location):
    location_flag = 'flags_small/' + location.lower().replace(' ', '-') + '.png'
    coviddata = find_country_coviddata_all(location)
    print(coviddata.values())
    labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in coviddata]
    values = [x.new_cases for x in coviddata]
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
               }
    print('service get_newcases_all()')
    return context


def get_totalcases_all(location):
    location_flag = 'flags_small/' + location.lower().replace(' ', '-') + '.png'
    coviddata = find_country_coviddata_all(location)
    labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in coviddata]
    labels = list(dict.fromkeys(labels))
    values = [x.total_cases for x in coviddata]
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
               }
    return context


def get_newdeaths_all(location):
    location_flag = 'flags_small/' + location.lower().replace(' ', '-') + '.png'
    coviddata = find_country_coviddata_all(location)
    labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in coviddata]
    labels = list(dict.fromkeys(labels))
    values = [x.new_deaths for x in coviddata]
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
               }
    return context


def get_totaldeaths_all(location):
    location_flag = 'flags_small/' + location.lower().replace(' ', '-') + '.png'
    coviddata = find_country_coviddata_all(location)
    labels = [x.date.strftime(COVID_DATE_LABELS_FMT) for x in coviddata]
    labels = list(dict.fromkeys(labels))
    values = [x.total_deaths for x in coviddata]
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
               }
    return context


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
