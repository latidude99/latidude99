#import django
#django.setup()

from owid.owid_country_dto import OwidCountryDTO
from owid.text_owid import *
from owid.repository_owid import *
from latidude99.settings import OWID_DATA_FOLDER, OWID_LOG_FOLDER
import datetime as dt
import pytz
import sys
import csv


owid_filein = OWID_DATA_FOLDER + COVID_COVID_DATA_CSV_FILE
d3_fileout_base = OWID_DATA_FOLDER + 'csv_d3_'

flouridh_fileout_base = OWID_DATA_FOLDER + 'csv_flourish_'


def convert_data_to_csv_race_flourish(flouridh_fileout_base, type):
    lines = []
    countries_obj = Country.objects.using('owid').all()
    data_world = CovidData.objects.using('owid').filter(country__location='World')
    date_line = ' ' + ', ' + ' '
    for d in data_world:
        date_line = date_line + ', ' + d.date.strftime('%d %b')
    lines.append(date_line)
    for c in countries_obj:
        line = c.location + ', ' + c.continent
        data = CovidData.objects.using('owid').filter(country__location=c.location)
        if type == 'totalcases':
            for d in data:
                if d.total_cases < 0:
                    d.total_cases = 0
                line = line + ', ' + str(int(d.total_cases))
        if type == 'totaldeaths':
            for d in data:
                if d.total_deaths < 0:
                    d.total_deaths = 0
                line = line + ', ' + str(int(d.total_deaths))
        lines.append(line)
        print(line)
    lines = lines[:-1]
    fileout = flouridh_fileout_base + type +'.csv'
    with open(fileout, mode='wt', encoding='utf-8') as fileout:
        fileout.write('\n'.join(lines))


def convert_csv_to_csv_race_d3(owid_filein, d3_fileout_base, type):
    data = []
    with open(owid_filein, newline='') as filein:
        linein_count = 0
        datareader = csv.reader(filein, delimiter=',')
        if type == 'totalcases':
            for row in datareader:
                line = row[3] + ', ' + row[2] + ', ' + row[4] + ', ' + row[1]
                data.append(line)
                linein_count += 1
    print(data[0])
    print('lines in: ' + str(linein_count))

    data = data[1:]
    fileout = d3_fileout_base + type +'.csv'
    with open(fileout, mode='wt', encoding='utf-8') as fileout:
        fileout.write('\n'.join(data))


ctx_base = {'style_css': STYLE_OWID,
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


# type: 'totalcases'
def get_data_d3race(type):
    fileout = d3_fileout_base + type + '.csv'
    convert_csv_to_csv_race_d3(owid_filein, d3_fileout_base, type)

    context = {
        'owid_data': OWID_DATA,
        'd3_csv_totalcases': fileout,

    }
    ctx = {**context, **ctx_base}
    return ctx






#convert_data_to_csv_race_flourish(flouridh_fileout_base, 'totalcases')
#convert_data_to_csv_race_flourish(flouridh_fileout_base, 'totaldeaths')









