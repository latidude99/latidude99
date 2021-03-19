# import django
# django.setup()

import random
import string
from snc.text import *
from snc.const import *
import snc.repository as repo
import snc.service_converters as service_converters
import snc.utils as utils
import snc.service_geojson as service_geojson



def get_base_context():
    context = {'title_tab': TITLE_TAB,
               'title_main': TITLE_MAIN,
               'back_pattern1': BACK_PATTERN1,
               }
    return context


def get_index_context():
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)
    context = {
        'catalogue': catalogueDTO,
        'google_api_key_dev_un': GOOGLE_API_KEY_DEV_UN,
        'google_api_key_dev': GOOGLE_API_KEY_DEV,
        'google_api_key_prod': GOOGLE_API_KEY_PROD,
               }
    ctx = {**get_base_context(), **context}
    return ctx


def get_charts_geojson_file_context():
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)

    # chartsDB = repo.find_charts_SCALE_2()
    # charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    # print('number of charts: ' + str(len(charts)))
    # #charts = repo.find_charts([4004])
    #
    # charts_geojson = service_geojson.generate_geojson(charts)

    charts_geojson = ''
    with open(SNC_GEOJSON_FILE, 'r') as reader:
        charts_geojson = reader.read()

    context = {
        'catalogue': catalogueDTO,
        'google_api_key_dev_un': GOOGLE_API_KEY_DEV_UN,
        'google_api_key_dev': GOOGLE_API_KEY_DEV,
        'google_api_key_prod': GOOGLE_API_KEY_PROD,
        'charts_geojson': charts_geojson,
               }
    ctx = {**get_base_context(), **context}
    return ctx


def get_charts_geojson_db_context(scale):
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)

    geojson = repo.find_geojson(scale)
    print(geojson)
    context = {
        'catalogue': catalogueDTO,
        'google_api_key_dev_un': GOOGLE_API_KEY_DEV_UN,
        'google_api_key_dev': GOOGLE_API_KEY_DEV,
        'google_api_key_prod': GOOGLE_API_KEY_PROD,
        'charts_geojson': geojson.json,
               }
    ctx = {**get_base_context(), **context}
    return ctx


def get_info_context():
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)
    context = {
        'catalogue': catalogueDTO,
               }
    ctx = {**get_index_context(), **context}
    return ctx


def get_search_multiple_context(nums):
    catalogueDB = repo.get_latest_catalogue()
    catalogue = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)
    print(nums)
    charts = []
    if len(nums) > 0 and len(nums) <= 15:
        for num in nums:
            if catalogueDB.chart_set.filter(number=num).exists():
                chartDB = catalogueDB.chart_set.get(number=num)
                chart = service_converters.chartDB_2_chartDTO(chartDB)
                charts.append(chart)
        context = {
            'catalogue': catalogue,
            'charts': charts,
            'search_multi_ok': 'Found ' + str(len(charts)) + ' chart(s)'
        }
    elif len(nums) > 15:
        nums_str = ''
        for n in nums:
            nums_str = nums_str + str(n) + ', '
        context = {
            'catalogue': catalogue,
            'charts': charts,
            'search_multi_ok': '',
            'search_multi_error': 'Maximum allowed number of charts is 15.',
            'search_multi_error1': 'You searched for ' + str(len(nums)) + ' charts.',
            'search_multi_error2': nums_str
        }
    else:
        nums_str = ''
        for n in nums:
            nums_str = nums_str + ', ' + str(n)
        context = {
            'catalogue': catalogue,
            'charts': charts,
            'search_multi_ok': '',
            'search_multi_error': 'No charts found for search term: ' + '\''+ nums_str + '\''
        }
    ctx = {**get_index_context(), **context}
    return ctx



def get_all_charts_context():
    chartsDB = repo.find_charts_all()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE1_charts_context():
    chartsDB = repo.find_charts_SCALE_1()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
        'search_multi_ok': 'Found ' + str(len(charts)) + ' chart(s)'
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE2_charts_context():
    chartsDB = repo.find_charts_SCALE_2()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE3_charts_context():
    chartsDB = repo.find_charts_SCALE_3()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE4_charts_context():
    chartsDB = repo.find_charts_SCALE_4()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE5_charts_context():
    chartsDB = repo.find_charts_SCALE_5()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE6_charts_context():
    chartsDB = repo.find_charts_SCALE_6()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE7_charts_context():
    chartsDB = repo.find_charts_SCALE_7()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx
