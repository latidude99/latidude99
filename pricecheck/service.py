# import django
# django.setup()

import random
import string
from pricecheck.text import *
from pricecheck.const import *

from pricecheck.service_converters import *


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
               'list_btn': LIST_BTN,
               }
    ctx = {**get_base_context(), **context}
    return ctx


def get_random_string(len):
    join = ''.join
    code = join(random.choices(string.ascii_letters, k=len))
    return code




