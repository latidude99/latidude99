import django

django.setup()

from owid.import_covid import *
from owid.text_owid import *
from main.send_email import *
from owid.repository_owid import *


def get_index_context():
    context = {'footer_info': FOOTER_INFO,
               'image': IMAGE_GLOBE,
               'background_pattern1': BACKGROUND_PATTERN1,
               'background_pattern2': BACKGROUND_PATTERN2,
               'latidude99': 'latidude99.com',
               'image_coronavirus': IMAGE_CORONAVIRUS,
               'covid_title': OWID_COVID_TITLE.title,
               'covid_subtitle': OWID_COVID_SUBTITLE,
               'covid_btn_txt': OWID_COVID_BTN_TXT,
               }
    return context








