#import django
#django.setup()

from pricecheck.text import *


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
               'time': TIME,
               'promo': PROMO,
               'promo_sub' :PROMO_SUB,
               'terms': TERMS,
               'error_1': ERROR_1,
               'error_3': ERROR_3,
               'validate_btn': VALIDATE_BTN,
               'submit_btn': SUBMIT_BTN,
               'confirm_btn': CONFIRM_BTN,
               'promo_btn': PROMO_BTN,

               }
    ctx = {**get_base_context(), **context}
    return ctx


def validate_url(url_text):
    tmp = '£133.99'
    validation = {}
    validation['product_name'] = 'Audio-Technica ATH-M50XBT Wireless Over-Ear Portable Headphones - Black'
    validation['product_price'] = float(tmp[1:])
    validation['product_currency'] = tmp[:1]
    return validation



#print(validate_url('aa'))