# import django
# django.setup()

from pricecheck.models import *
import requests
from bs4 import BeautifulSoup
import pricecheck.service_email
import latidude99.settings as settings
import datetime as dt
import pytz
from django.utils import timezone
from pricecheck.text import *
from pricecheck.const import *
from pricecheck.models import *
from pricecheck.dto import *
from pricecheck.service_converters import *
import string, random


def get_base_context():
    context = {'title_tab': TITLE_TAB,
               'title_main': TITLE_MAIN,
               'back_pattern1': BACK_PATTERN1,
               }
    return context


def get_index_context():
    context = {'welcome_text': WELCOME_TEXT,
               'link': LINK,
               'name': NAME,
               'email': EMAIL,
               'url': URL,
               'duration': DURATION,
               'promo': PROMO,
               'promo_sub': PROMO_SUB,
               'terms': TERMS,
               'error_1': ERROR_1,
               'error_3': ERROR_3,
               'validate_btn': VALIDATE_BTN,
               'submit_btn': SUBMIT_BTN,
               'confirm_btn': CONFIRM_BTN,
               'promo_btn': PROMO_BTN,
               'track_btn': TRACK_BTN,
               'stop_btn': STOP_BTN,
               }
    ctx = {**get_base_context(), **context}
    return ctx


def get_random_string_16():
    join = ''.join
    code = join(random.choices(string.ascii_letters, k=16))
    return code




