# import django
# django.setup()

from owid.text_owid import *
from owid.text_cia import *


def get_cia_base_context():
    context = {'image': IMAGE_GLOBE_BIG,
               'background_pattern1': BACKGROUND_PATTERN1,
               'background_pattern2': BACKGROUND_PATTERN2,
               'background_pattern3': BACKGROUND_PATTERN3,
               'background_pattern4': BACKGROUND_PATTERN4,
               'background_pattern5': BACKGROUND_PATTERN5,
               'background_pattern6': BACKGROUND_PATTERN6,
               'background_pattern7': BACKGROUND_PATTERN7,
               'background_pattern8': BACKGROUND_PATTERN8,
               'background_pattern9': BACKGROUND_PATTERN9,
               'background_pattern10': BACKGROUND_PATTERN10,
               'background_pattern11': BACKGROUND_PATTERN11,
               'latidude99': 'latidude99.com',
               'title': CIA_TITLE,
               'subtitle': CIA_SUBTITLE,
               'btn_txt': CIA_BTN_TXT,
               'select_country': SELECT_COUNTRY,
               }
    return context


def get_cia_context():
    context = {'info0': CIA_INFO0,
               'info1': CIA_INFO1,
               'info2': CIA_INFO2,
               }
    ctx = {**get_cia_base_context(), **context}
    return ctx


def get_cia_country_context():
    context = {
    }
    ctx = {**get_cia_base_context(), **context}
    return ctx
