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
from pricecheck.models import *
from pricecheck.dto import *
import string, random

name_tag = AMAZON_NAME_ID
price_tags = AMAZON_PRICE_IDS

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


def get_product_info_context(product):
    product_dto = get_product_info(product)
    context = {'product_dto': product_dto,
               'product_info_1': PRODUCT_INFO_1,
               'product_info_2': PRODUCT_INFO_2,
               'product_info_3': PRODUCT_INFO_3,
               'product_info_4': PRODUCT_INFO_4,
               'product_info_5': PRODUCT_INFO_5,
               'product_info_6': PRODUCT_INFO_6,

               }
    ctx = {**get_base_context(), **context}
    return ctx


def update_prices(track_code):
    code = track_code.strip()
    if code != '' and len(code) < 16:
        error = code + ' - Invalid tracking code: the code has to be 16 characters long.'
        return error
    elif len(code) == 16:
        try:
            product = Product.objects.using('pricecheck_34').get(track_code=code)
            current_price = check_price(product,AMAZON_NAME_ID, AMAZON_PRICE_IDS)
            price = Price(product=product, price=current_price[1:], date=dt.timezone.now, currency=current_price[0])
            price.save(using='pricecheck_34')
            return code + ' product price updated.'
        except Product.DoesNotExist:
            error = code + ' - Invalid tracking code: no product found.'
            return error
    else:
        products = Product.objects.using('pricecheck_34').filter(tracked=True)
        for product in products:
            current_price = check_price(product, AMAZON_NAME_ID, AMAZON_PRICE_IDS)
            price = Price(product=product,
                          price=current_price[1:],
                          date=dt.datetime.utcnow().replace(tzinfo=pytz.UTC),
                          currency=current_price[0])
            price.save(using='pricecheck_34')

        return str(len(products)) + ' products prices updated.'


def check_price(product, name_tag, price_tags):
    product_name = ''
    product_price = ''

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(product.url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    div_product = soup.find(id=name_tag)
    div_price = None
    for id in price_tags:
        div_price = soup.find(id=id)
        if div_price != None:  # found the working price tag
            break
    if div_price != None:
        product_name = div_product.get_text().strip()
        product_price = div_price.get_text().strip()
    return product_price


def get_product_info(product_dto):
    code = product_dto.track_code.strip()
    if len(code) < 16:
        product_dto.error = code + ' - Invalid tracking code: the code has to be 16 characters long.'
        return product_dto
    try:
        product_db = Product.objects.using('pricecheck_34').get(track_code=code)
        user = product_db.user
        product_dto.username = user.name
        product_dto.email = user.email
        product_dto.product_max_count = MAX_PRODUCT_TRACKED
        product_dto.product_count = user.product_set.filter(tracked=True).count()
        product_dto.name = product_db.name
        product_dto.initial_price = product_db.initial_price
        product_dto.currency = product_db.initial_currency

        product_dto.start_date = product_db.start_date.strftime('%d %B %Y, %H:%M')
        product_dto.end_date = product_db.end_date.strftime('%d %B %Y, %H:%M')
        timedelta = product_db.end_date - dt.datetime.utcnow().replace(tzinfo=pytz.UTC)
        product_dto.duration_left = str(timedelta.days)

        prices = product_db.price_set.all()
        price_labels = [x.date.strftime('%d %b %Y, %H:%M') for x in prices]
        price_values = [x.price for x in prices]
        product_dto.current_price = price_values[-1]

        labels_filler = ['waiting'] * (timedelta.days * 3)
        values_filler = [0] * (timedelta.days * 3)
        product_dto.price_labels = price_labels + labels_filler
        product_dto.price_values = price_values + values_filler

        product_dto.track_code = product_db.track_code
        product_dto.stop_code = product_db.stop_code
        product_dto.duration = str(product_db.duration) + ' day(s)'
        product_dto.threshold_up = product_dto.currency + str(product_db.threshold_up)
        product_dto.threshold_down = product_dto.currency + str(product_db.threshold_down)

        if product_db.tracked:
            product_dto.status = 'Tracked'
        else:
            product_dto.status = 'Not tracked'

    except Product.DoesNotExist:
        product_dto.error = code + ' - Invalid tracking code: no product found.'
        return product_dto

    return product_dto


def get_add_product_context(user, product):
    product_dto = add_product(user, product)
    context = {'product_dto': product_dto,
               'success_info_1': SUCCESS_INFO_1,
               'success_info_2': SUCCESS_INFO_2,
               'success_info_3': SUCCESS_INFO_3,
               'success_info_4': SUCCESS_INFO_4,
               'success_info_5': SUCCESS_INFO_5,
               'success_info_6': SUCCESS_INFO_6,

               }
    ctx = {**get_base_context(), **context}
    return ctx


def user_limit_duplicate_check(product_dto):
    if not User.objects.using('pricecheck_34').filter(email=product_dto.email).exists():
        user = User()
        user.name = product_dto.username
        user.email = product_dto.email
        user.save(using='pricecheck_34')
        return [True, user]
    else:
        user = User.objects.using('pricecheck_34').get(email=product_dto.email)
        product_count = user.product_set.filter(tracked=True).count()
        product_exist = user.product_set.filter(url=product_dto.url, tracked=True).count()
        errors = {}
        if product_count >= MAX_PRODUCT_TRACKED:
            errors['error1'] = 'You are tracking ' + str(product_count) + ' products. This is the maximum number ' \
                                 'of items allowed to be tracked simultaneously by '
            errors['error2'] = 'You can stop tracking one of the products to start tracking a new one. To stop tracking ' \
                                'any product please click on the relevant Stop Tracking link in the last email.'
            errors['error3'] = 'Alternatively, you can buy me a coffee (link on the home page) and gain access to larger ' \
                                'number of tracked items as well as longer tracking times and setting price change thresholds'
            return [False, errors]
        elif product_exist > 0:
            errors['error1'] = 'You are already tracking a product with the same URL'
            product = user.product_set.get(url=product_dto.url, tracked=True)
            errors['error2'] = 'You can check the detals entering this product tracking code on home page: '
            errors['error3'] = ''
            errors['error4'] = product.track_code
            return [False, errors]


def add_product(user, product_dto):
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
    product_db.tracked = True

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
    product_dto.product_max_count = MAX_PRODUCT_TRACKED
    product_dto.product_count = user.product_set.filter(tracked=True).count()
    product_dto.start_date = product_db.start_date.strftime('%d %B %Y, %H:%M')
    product_dto.end_date = product_db.end_date.strftime('%d %B %Y, %H:%M')
    product_dto.track_code = product_db.track_code
    product_dto.stop_code = product_db.stop_code
    product_dto.duration = str(product_db.duration) + ' day(s)'
    product_dto.threshold_up = product_dto.currency + str(product_db.threshold_up)
    product_dto.threshold_down = product_dto.currency + str(product_db.threshold_down)

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




