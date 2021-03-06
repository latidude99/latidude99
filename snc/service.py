# import django
# django.setup()

import random
import string
from snc.text import *
from snc.const import *
import snc.repository as repo
import snc.service_converters as service_converters
import snc.service_geojson_chs as service_geojson_chs
from snc.chart import *
import snc.utils as utils
import snc.service_geojson as service_geojson
import datetime as dt
import locale

locale.setlocale(locale.LC_ALL, '')


def get_base_context():
    context = {'title_tab': TITLE_TAB,
               'title_main': TITLE_MAIN,
               'back_pattern1': BACK_PATTERN1,
               'scale1': SCALE_1_TEXT,
               'scale2': SCALE_2_TEXT,
               'scale3': SCALE_3_TEXT,
               'scale4': SCALE_4_TEXT,
               'scale5': SCALE_5_TEXT,
               'scale6': SCALE_6_TEXT,
               'scale7': SCALE_7_TEXT,
               'scale0': SCALE_ALL_TEXT,
               'map_zoom': MAP_ZOOM,
               'map_zoom_chs': MAP_ZOOM_CHS,
               'map_centre': MAP_CENTRE,
               'map_centre_chs': MAP_CENTRE_CHS,
               'map_bounds': MAP_BOUNDS,
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


def get_info_context():
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)
    context = {
        'catalogue': catalogueDTO,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_chs_index_context():
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


# ------------------------- chs geojson ---------------------------------

def get_chs_catalogue_info_context():
    geojson = repo.find_geojson_chs_scale_range()
    import_date = geojson.import_date
    import_date_short = import_date.strftime('%B %Y')

    context_chs_catalogue = {
        'catalogue_id': geojson.id,
        'import_date': geojson.import_date,
        'import_date_short': import_date_short,
        'total_chart_count': geojson.total_chart_count,
    }
    return context_chs_catalogue

# fetches chs geojson from db
def get_charts_chs_geojson_db_split_scale_context():
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)

    context_main = {
        'catalogue': catalogueDTO,
        'google_api_key_dev_un': GOOGLE_API_KEY_DEV_UN,
        'google_api_key_dev': GOOGLE_API_KEY_DEV,
        'google_api_key_prod': GOOGLE_API_KEY_PROD,
    }

    geojson = repo.find_geojson_chs_scale_range()
    import_date = geojson.import_date
    import_date_short = import_date.strftime('%B %Y')

    context_geojson = {
        'geojson_scale_1': geojson.json_scale_1,
        'geojson_scale_2': geojson.json_scale_2,
        'geojson_scale_3': geojson.json_scale_3,
        'geojson_scale_4': geojson.json_scale_4,
        'geojson_scale_5': geojson.json_scale_5,
        'catalogue_id': geojson.id,
        'import_date': geojson.import_date,
        'import_date_short': import_date_short,
        'total_chart_count': geojson.total_chart_count,
        'scale_1': CHS_SCALE_1,
        'scale_2': CHS_SCALE_2,
        'scale_3': CHS_SCALE_3,
        'scale_4': CHS_SCALE_4,
    }
    context_scale_ranges_check = {'sc1checked': 'checked',
                              'sc2checked': 'checked',
                              'sc3checked': 'checked',
                              'sc4checked': 'checked',
                              'sc5checked': 'checked',
                              }

    ctx = {**get_base_context(), **context_main, **context_geojson, **context_scale_ranges_check}
    return ctx


# fetches chs geojson from file located in snc/data/
def get_charts_chs_geojson_file_split_scale_context(file_path):
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)

    # charts_geojson = ''
    # with open(CHS_GEOJSON_FILE_SCALE_1, 'r') as reader:
    #     charts_geojson = reader.read()

    context_main = {
        'catalogue': catalogueDTO,
        'google_api_key_dev_un': GOOGLE_API_KEY_DEV_UN,
        'google_api_key_dev': GOOGLE_API_KEY_DEV,
        'google_api_key_prod': GOOGLE_API_KEY_PROD,
        # 'charts_geojson': charts_geojson,
    }
    context_geojson = service_geojson_chs.create_split_scale_geojson_context(CHS_GEOJSON_FILE)
    ctx = {**get_base_context(), **context_main, **context_geojson}
    return ctx


# fetches chs geojson from file located in snc/data/
def get_charts_chs_geojson_file_context(file_path):
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)

    charts_geojson = ''
    with open(file_path, 'r') as reader:
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


# ------------------------- snc geojson ---------------------------------

def get_chart_single_geojson_db_context(num):
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)

    geojson = repo.find_geojson_single(num)
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


def get_chart_multi_geojson_db_context(nums):
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)

    geojson = repo.find_geojson_multiple(nums)
    # print('---')
    # print(geojson)
    context = {
        'catalogue': catalogueDTO,
        'google_api_key_dev_un': GOOGLE_API_KEY_DEV_UN,
        'google_api_key_dev': GOOGLE_API_KEY_DEV,
        'google_api_key_prod': GOOGLE_API_KEY_PROD,
        'charts_geojson': geojson,
    }
    ctx = {**get_base_context(), **context}
    return ctx


def get_charts_geojson_scale_range_all_split_scales_db_context(scale_range):
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)

    # dict of geojsons for each scale range
    geojson = repo.find_geojson_scale_range_all_split_scales(catalogueDB)

    # check boxes in charts.html
    ctx_scale_ranges_check = {'sc1checked': 'checked',
                              'sc2checked': 'checked',
                              'sc3checked': 'checked',
                              'sc4checked': 'checked',
                              'sc5checked': 'checked',
                              'sc6checked': 'checked',
                              'sc7checked': ''
                              }

    ctx_scale_ranges = {'sc1_const': SCALE_1_TEXT,
                        'sc2_const': SCALE_2_TEXT,
                        'sc3_const': SCALE_3_TEXT,
                        'sc4_const': SCALE_4_TEXT,
                        'sc5_const': SCALE_5_TEXT,
                        'sc6_const': SCALE_6_TEXT,
                        'sc7_const': SCALE_7_TEXT,
                        }

    # print(geojson)
    context = {
        'catalogue': catalogueDTO,
        'google_api_key_dev_un': GOOGLE_API_KEY_DEV_UN,
        'google_api_key_dev': GOOGLE_API_KEY_DEV,
        'google_api_key_prod': GOOGLE_API_KEY_PROD,
        'charts_geojson_scale_1': geojson['scale1'],
        'charts_geojson_scale_2': geojson['scale2'],
        'charts_geojson_scale_3': geojson['scale3'],
        'charts_geojson_scale_4': geojson['scale4'],
        'charts_geojson_scale_5': geojson['scale5'],
        'charts_geojson_scale_6': geojson['scale6'],
        'charts_geojson_scale_7': geojson['scale7'],
        'charts_geojson_scale_8XXX': geojson['8XXX'],

    }
    ctx = {**get_base_context(), **context, **ctx_scale_ranges_check, **ctx_scale_ranges, **get_chs_catalogue_info_context()}
    return ctx


def get_charts_geojson_scale_range_single_db_context(scale_range):
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)

    geojson = repo.find_geojson_scale_range_single(catalogueDB, scale_range)

    ctx_scale_ranges = {'sc1checked': 'checked',
                        'sc2checked': 'checked',
                        'sc3checked': 'checked',
                        'sc4checked': 'checked',
                        'sc5checked': 'checked',
                        'sc6checked': 'checked',
                        'sc7checked': 'checked'
                        }

    # print(geojson)
    context = {
        'catalogue': catalogueDTO,
        'google_api_key_dev_un': GOOGLE_API_KEY_DEV_UN,
        'google_api_key_dev': GOOGLE_API_KEY_DEV,
        'google_api_key_prod': GOOGLE_API_KEY_PROD,
        'charts_geojson': geojson.json,
    }
    ctx = {**get_base_context(), **context, **ctx_scale_ranges}
    return ctx


def get_charts_geojson_scale_range_multiple_db_context(scale_ranges):
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)

    geojson = repo.find_geojson_scale_range_multiple(catalogueDB, scale_ranges)

    ctx_scale_ranges = {}
    if SCALE_1_TEXT in scale_ranges:
        ctx_scale_ranges['sc1checked'] = 'checked'
    if SCALE_2_TEXT in scale_ranges:
        ctx_scale_ranges['sc2checked'] = 'checked'
    if SCALE_3_TEXT in scale_ranges:
        ctx_scale_ranges['sc3checked'] = 'checked'
    if SCALE_4_TEXT in scale_ranges:
        ctx_scale_ranges['sc4checked'] = 'checked'
    if SCALE_5_TEXT in scale_ranges:
        ctx_scale_ranges['sc5checked'] = 'checked'
    if SCALE_6_TEXT in scale_ranges:
        ctx_scale_ranges['sc6checked'] = 'checked'
    if SCALE_7_TEXT in scale_ranges:
        ctx_scale_ranges['sc7checked'] = 'checked'

    # print(geojson)
    context = {
        'catalogue': catalogueDTO,
        'google_api_key_dev_un': GOOGLE_API_KEY_DEV_UN,
        'google_api_key_dev': GOOGLE_API_KEY_DEV,
        'google_api_key_prod': GOOGLE_API_KEY_PROD,
        'charts_geojson': geojson,
    }
    ctx = {**get_base_context(), **context, **ctx_scale_ranges}
    return ctx


# fetches geojson from file located in snc/data/
def get_charts_geojson_file_context(file_name):
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)

    file_path = SNC_DATA_FOLDER + file_name
    charts_geojson = ''
    with open(file_path, 'r') as reader:
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



# ------------------------- chartDTO ---------------------------------

def get_single_context(num):
    chart = ChartDTO()
    catalogueDB = repo.get_latest_catalogue()
    catalogue = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)
    if catalogueDB.chart_set.filter(number=num).exists():
        chartDB = catalogueDB.chart_set.get(number=num)
        chart = service_converters.chartDB_2_chartDTO(chartDB)
    return chart


def chartDTO_2_chartJSON(ch):
    panels = []
    if len(ch.panels) > 0:
        for p in ch.panels:
            panel = {'id': p.panel_id,
                     'name': p.name,
                     'scale': '1 : ' + f'{int(p.scale):n}',
                     }
            panels.append(panel)

    notices = []
    if len(ch.notices) > 0:
        for n in ch.notices:
            notice = {'year': n.year,
                      'week': n.week,
                      'number': n.number,
                      'type': n.type
                      }
            notices.append(notice)
    scale = ''
    if ch.scale != '':
        scale = '1 ' + f'{int(ch.scale):n}'
    else:
        scale = 'no main polygon'
    chartJSON = {
        'catalogue_id': ch.catalogue_id,
        'number': ch.number,
        'title': ch.title,
        'scale': scale,
        'status': ch.status,
        'status_date': ch.status_date,
        'new_edition_date': ch.new_edition_date,
        'last_nm_number': ch.last_nm_number,
        'last_nm_date': ch.last_nm_date,
        'max_scale_category': ch.max_scale_category,
        'zoom_min': ch.zoom_min,
        'zoom_max': ch.zoom_max,
        'colour': ch.colour,
        'zindex': ch.zindex,
        'panels': panels,
        'notices': notices,
    }

    return chartJSON


def get_search_multiple_context(nums):
    catalogueDB = repo.get_latest_catalogue()
    catalogue = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)
    # print(nums)
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
            'search_multi_error': 'No charts found for search term: ' + '\'' + nums_str + '\''
        }
    ctx = {**get_index_context(), **context, **get_chs_catalogue_info_context()}
    return ctx


def get_all_charts_context():
    chartsDB = repo.find_charts_all()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    # print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE1_charts_context():
    chartsDB = repo.find_charts_SCALE_1()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    # print('number of charts: ' + str(len(charts)))
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
    # print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE3_charts_context():
    chartsDB = repo.find_charts_SCALE_3()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    # print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE4_charts_context():
    chartsDB = repo.find_charts_SCALE_4()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    # print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE5_charts_context():
    chartsDB = repo.find_charts_SCALE_5()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    # print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE6_charts_context():
    chartsDB = repo.find_charts_SCALE_6()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    # print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx


def get_SCALE7_charts_context():
    chartsDB = repo.find_charts_SCALE_7()
    charts = service_converters.chartsDB_2_chartsDTO(chartsDB)
    # print('number of charts: ' + str(len(charts)))
    context = {
        'catalogue': charts[0].catalogue_id,
        'charts': charts,
    }
    ctx = {**get_index_context(), **context}
    return ctx
