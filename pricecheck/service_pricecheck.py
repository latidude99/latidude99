# import django
# django.setup()

from pricecheck.models import *
import requests
from bs4 import BeautifulSoup
import pricecheck.service_email
import latidude99.settings as settings
import datetime as dt
import pytz
from pricecheck.text import *
from pricecheck.models import *
from pricecheck.dto import *
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

               }
    ctx = {**get_base_context(), **context}
    return ctx


def validate_url(url, product_id, price_ids):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    div_product = soup.find(id=product_id)
    div_price = None
    for id in price_ids:
        div_price = soup.find(id=id)
        if div_price != None:  # found the working price tag
            break
    print(url)
    print(product_id)
    print(price_ids)
    print(div_price)
    validation = {}
    if div_price != None:
        product_name = div_product.get_text().strip()
        product_price = div_price.get_text().strip()
        validation['product_name'] = product_name
        validation['product_price'] = product_price[1:]
        validation['product_currency'] = product_price[:1]
        validation['error'] = None
    else:
        validation['product_name'] = ''
        validation['product_price'] = ''
        validation['product_currency'] = ''
        validation['error'] = 'No price found'
    return validation


def get_add_product_context(product):
    product_db = add_product(product)
    context = {'product_db': product_db,
               'success_info_1': SUCCESS_INFO_1,
               'success_info_2': SUCCESS_INFO_2,
               'success_info_3': SUCCESS_INFO_3,
               'success_info_4': SUCCESS_INFO_4,
               'success_info_5': SUCCESS_INFO_5,
               'success_info_6': SUCCESS_INFO_6,

               }
    ctx = {**get_base_context(), **context}
    return ctx

'''
      
'''


def add_product(product_dto):
    if not User.objects.using('pricecheck_34').filter(email=product_dto.email).exists():
        user = User()
        user.name = product_dto.username
        user.email = product_dto.email
        user.save(using='pricecheck_34')
    else:
        user = User.objects.using('pricecheck_34').get(email=product_dto.email)

    product_db = Product()
    product_db.user = user
    product_db.url = product_dto.url
    product_db.name = product_dto.name
    start_date = dt.datetime.utcnow().replace(tzinfo=pytz.UTC)
    product_db.start_date = start_date
    product_db.duration = product_dto.duration
    product_db.end_date = start_date + dt.timedelta(days=int(product_dto.duration))
    product_db.initial_price = float(product_dto.price)
    product_db.initial_currency = product_dto.currency
    product_db.validated = True
    product_db.traced = True

    track_code = get_random_string_16()
    while Product.objects.using('pricecheck_34').filter(track_code=track_code).exists():
        track_code = get_random_string_16()
    product_db.track_code = track_code

    stop_code = get_random_string_16()
    while Product.objects.using('pricecheck_34').filter(track_code=stop_code).exists():
        stop_code = get_random_string_16()
    product_db.stop_code = stop_code

    product_db.save(using='pricecheck_34')

    price = Price()
    price.product = product_db
    price.date = product_db.start_date
    price.price = product_db.initial_price
    price.currency = product_db.initial_currency

    promocode = product_dto.promocode # to do: check/setup Voucher code

    price.save(using='pricecheck_34')

    # back to view
    product_dto.start_date = product_db.start_date.strftime('%d %B %Y, %H:%M')
    product_dto.end_date = product_db.end_date.strftime('%d %B %Y, %H:%M')
    product_dto.track_code = product_db.track_code
    product_dto.stop_code = product_db.stop_code
    product_dto.duration = str(product_db.duration) + ' day(s)'

    return product_dto



def get_random_string_16():
    join = ''.join
    code = join(random.choices(string.ascii_letters, k=16))
    return code






'''

def check():
    context = check_item_price(get_page_html(user.url))
    print(context)
    subject = 'Price check for ' + context['product']
    template = 'pricecheck/email_templ_1.html'
    sender = settings.EMAIL_HOST_USER
    receiver = user.email
    pricecheck.service_email.send(subject, template, context, sender, receiver)
    print('pricecheck email sent to ' + user.email)
    
'''




