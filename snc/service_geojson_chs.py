import copy

#import django
#django.setup()

from icecream import ic

import snc.service_converters as service_converters
import snc.repository as repo
from snc.models import *
from geojson import Point, Polygon, MultiPolygon, Feature, FeatureCollection, dump
import json
from snc.text import *
from snc.const import *
from snc.chart import *
from snc.position import *
import datetime as dt
import pytz
import locale


def parse_edit_import_to_db_geojson_chs(file):
    with open(file) as json_file:
        data = json.load(json_file)
        print(data['type'])
        prev = ''
        for f in data['features']:
            curr = f['properties']['TITLE'].split(' ')[0][:-1]
            if curr == prev:
                i = i + 1
            else:
                i=1
            f['properties']['CHART'] = curr + 'panel' + str(i)
            prev = curr

    data_scale_1 = copy.deepcopy(data)
    data_scale_2 = copy.deepcopy(data)
    data_scale_3 = copy.deepcopy(data)
    data_scale_4 = copy.deepcopy(data)
    data_scale_5 = copy.deepcopy(data)

    data_scale_1['features'][:] = [x for x in data_scale_1['features'] if x['properties']['PC_MIN_SCALE'] <= CHS_SCALE_1]
    data_scale_2['features'][:] = [x for x in data_scale_2['features'] if (x['properties']['PC_MIN_SCALE'] > CHS_SCALE_1 and x['properties']['PC_MIN_SCALE'] <= CHS_SCALE_2)]
    data_scale_3['features'][:] = [x for x in data_scale_3['features'] if (x['properties']['PC_MIN_SCALE'] > CHS_SCALE_2 and x['properties']['PC_MIN_SCALE'] <= CHS_SCALE_3)]
    data_scale_4['features'][:] = [x for x in data_scale_4['features'] if (x['properties']['PC_MIN_SCALE'] > CHS_SCALE_3 and x['properties']['PC_MIN_SCALE'] <= CHS_SCALE_4)]
    data_scale_5['features'][:] = [x for x in data_scale_5['features'] if x['properties']['PC_MIN_SCALE'] > CHS_SCALE_4]

    geojson_chs = GeojsonCHS()
    geojson_chs.import_date = dt.datetime.now(pytz.timezone('Europe/London'))
    geojson_chs.json_scale_1 = json.dumps(data_scale_1)
    geojson_chs.json_scale_1 = json.dumps(data_scale_2)
    geojson_chs.json_scale_1 = json.dumps(data_scale_3)
    geojson_chs.json_scale_1 = json.dumps(data_scale_4)
    geojson_chs.json_scale_1 = json.dumps(data_scale_5)
    # geojson_chs.json_scale_all = json.dumps(data)
    geojson_chs.type = 'scale_range'
    geojson_chs.ready = True
    geojson_chs.save(using=DB_SNC)

    return True




# adds unique chart number for each paper chart and its panels
def read_and_edit_geojson_chs(file):
    with open(file) as json_file:
        data = json.load(json_file)
        print(data['type'])
        prev = ''
        for f in data['features']:
            curr = f['properties']['TITLE'].split(' ')[0][:-1]
            if curr == prev:
                i = i + 1
            else:
                i=1
            # print(f['type'])
            # print(f['properties']['NAME'])
            # print(f['properties']['TITLE'])
            # print(f['properties']['TITLE'].split(' ')[0][:-1])
            f['properties']['CHART'] = curr + 'panel' + str(i)
            # print(f['properties']['CHART'])
            # print(f['properties']['SCALE'])
            # print('')
            prev = curr
    with open(CHS_GEOJSON_FILE_EDITED, 'w') as outfile:
        json.dump(data, outfile)
    print('all charts ' + str(len(data['features'])))
    return data


def create_split_scale_geojson_context(chs_file):
    data = read_and_edit_geojson_chs(chs_file)
    data_scale_1 = copy.deepcopy(data)
    data_scale_2 = copy.deepcopy(data)
    data_scale_3 = copy.deepcopy(data)
    data_scale_4 = copy.deepcopy(data)
    data_scale_5 = copy.deepcopy(data)

    # print(len(data_scale_1['features']))
    # print(len(data_scale_2['features']))

    data_scale_1['features'][:] = [x for x in data_scale_1['features'] if x['properties']['PC_MIN_SCALE'] <= CHS_SCALE_1]
    data_scale_2['features'][:] = [x for x in data_scale_2['features'] if (x['properties']['PC_MIN_SCALE'] > CHS_SCALE_1 and x['properties']['PC_MIN_SCALE'] <= CHS_SCALE_2)]
    data_scale_3['features'][:] = [x for x in data_scale_3['features'] if (x['properties']['PC_MIN_SCALE'] > CHS_SCALE_2 and x['properties']['PC_MIN_SCALE'] <= CHS_SCALE_3)]
    data_scale_4['features'][:] = [x for x in data_scale_4['features'] if (x['properties']['PC_MIN_SCALE'] > CHS_SCALE_3 and x['properties']['PC_MIN_SCALE'] <= CHS_SCALE_4)]
    data_scale_5['features'][:] = [x for x in data_scale_5['features'] if x['properties']['PC_MIN_SCALE'] > CHS_SCALE_4]
    print(len(data_scale_1['features']))
    print(len(data_scale_2['features']))
    print(len(data_scale_3['features']))
    print(len(data_scale_4['features']))
    print(len(data_scale_5['features']))

   # print(json.dumps(data_scale_1))

    # with open(CHS_GEOJSON_FILE_SCALE_1, 'w') as outfile:
    #     json.dump(data_scale_1, outfile)

    context = {
        'geojson_scale_1': json.dumps(data_scale_1),
        'geojson_scale_2': json.dumps(data_scale_2),
        'geojson_scale_3': json.dumps(data_scale_3),
        'geojson_scale_4': json.dumps(data_scale_4),
        'geojson_scale_5': json.dumps(data_scale_5),
    }

    return context


# filters geojson according to min chart scale (in place)
def filter_geojson_chs(file, chs_scale_range):
    with open(file) as json_file:
        data = json.load(json_file)
        print(data['type'])
    data['features'][:] = [x for x in data['features'] if x['properties']['PC_MIN_SCALE'] < chs_scale_range]
    with open(file[:-8] + '_0-20k.geojson', 'w') as outfile:
        json.dump(data, outfile)
    return data










