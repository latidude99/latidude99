# import django
# django.setup()

import random
import string
from snc.text import *
from snc.const import *
import snc.repository as repo
import snc.service_converters as service_converters
import snc.utils as utils



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


def get_info_context():
    catalogueDB = repo.get_latest_catalogue()
    catalogueDTO = service_converters.catalogueDB_2_catalogueDTO(catalogueDB)
    context = {
        'catalogue': catalogueDTO,
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
