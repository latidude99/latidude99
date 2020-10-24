#import django
#django.setup()

from owid.text_owid import *


def get_index_context():
    context = {'owid_title': OWID_TITLE,
               'image': IMAGE_GLOBE,
               'background_pattern1': BACKGROUND_PATTERN1,
               'background_pattern2': BACKGROUND_PATTERN2,
               'background_pattern3': BACKGROUND_PATTERN3,
               'background_pattern4': BACKGROUND_PATTERN4,
               'background_pattern5': BACKGROUND_PATTERN5,
               'latidude99': 'latidude99.com',
               'image_coronavirus': IMAGE_CORONAVIRUS,
               'covid_title': OWID_COVID_TITLE.title,
               'covid_subtitle': OWID_COVID_SUBTITLE,
               'covid_btn_txt': OWID_COVID_BTN_TXT,
               'image_cia': IMAGE_CIA,
               'cia_title': OWID_CIA_TITLE.title,
               'cia_subtitle': OWID_CIA_SUBTITLE,
               'cia_btn_txt': OWID_CIA_BTN_TXT,
               }
    return context
