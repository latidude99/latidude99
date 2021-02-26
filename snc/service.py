# import django
# django.setup()

import random
import string
from snc.text import *
from snc.const import *



def get_base_context():
    context = {'title_tab': TITLE_TAB,
               'title_main': TITLE_MAIN,
               'back_pattern1': BACK_PATTERN1,
               }
    return context


def get_index_context():
    context = {
        'google_api_key_dev_un': GOOGLE_API_KEY_DEV_UN,
        'google_api_key_dev': GOOGLE_API_KEY_DEV,
        'google_api_key_prod': GOOGLE_API_KEY_PROD,
               }
    ctx = {**get_base_context(), **context}
    return ctx


def get_random_string(len):
    join = ''.join
    code = join(random.choices(string.ascii_letters, k=len))
    return code




