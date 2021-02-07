# import django
# django.setup()

from pricecheck.models import *
import requests
from bs4 import BeautifulSoup
import pricecheck.service_email
import pricecheck.service as service
import pricecheck.service_info as service_info
import pricecheck.service_track as service_track
import pricecheck.service_converters as service_converters
import latidude99.settings as settings
import datetime as dt
import pytz
from django.utils import timezone
from pricecheck.text import *
from pricecheck.models import *
from pricecheck.dto import *
import string, random


def user_limit_duplicate_check(product_dto):
    if not User.objects.using('pricecheck_34').filter(email=product_dto.email).exists():
        user = User()
        user.name = product_dto.username
        user.email = product_dto.email
        user.save(using='pricecheck_34')
        return [True, user]
    else:
        user = User.objects.using('pricecheck_34').get(email=product_dto.email)
        products_tracked_count = user.product_set.filter(tracked=True).count()
        product_tracked = user.product_set.filter(url=product_dto.url, tracked=True).count()

        errors = {}
        if products_tracked_count >= MAX_PRODUCT_TRACKED:
            errors['error1'] = 'You are tracking ' + str(product_count) + ' products. This is the maximum number ' \
                                 'of items allowed to be tracked simultaneously by '
            errors['error2'] = 'You can stop tracking one of the products to start tracking a new one. To stop tracking ' \
                                'any product please click on the relevant Stop Tracking link in the last email.'
            errors['error3'] = 'Alternatively, you can buy me a coffee (link on the home page) and gain access to larger ' \
                                'number of tracked items as well as longer tracking times and setting price change thresholds'
            return [False, errors]
        elif product_tracked > 0:
            errors['error1'] = 'You are already tracking a product with the same URL'
            product = user.product_set.get(url=product_dto.url, tracked=True)
            errors['error2'] = 'You can check the detals entering this product tracking code on home page: '
            errors['error3'] = ''
            errors['error4'] = product.track_code
            return [False, errors]

    return [True, user]


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
    ctx = {**service.get_base_context(), **context}
    return ctx


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

    track_code = service.get_random_string(16)
    while Product.objects.using('pricecheck_34').filter(track_code=track_code).exists():
        track_code = service.get_random_string(16)
    product_db.track_code = track_code

    stop_code = service.get_random_string(16)
    while Product.objects.using('pricecheck_34').filter(track_code=stop_code).exists():
        stop_code = service.get_random_string(16)
    product_db.stop_code = stop_code

    confirm_code = service.get_random_string(32)
    while Product.objects.using('pricecheck_34').filter(track_code=stop_code).exists():
        confirm_code = service.get_random_string(32)
    product_db.confirm_code = confirm_code

    product_db.confirm_code = confirm_code
    product_db.confirm_link = APP_BASE + '/confirm_product?code=' + confirm_code

    product_db.save(using='pricecheck_34')

    product_dto.track_link = APP_BASE + '/confirm_product?code=' + track_code
    product_dto.stop_link = APP_BASE + '/confirm_product?code=' + stop_code
    product_dto.app_link = APP_BASE

    price = Price()
    price.product = product_db
    price.date = product_db.start_date
    price.price = product_db.initial_price
    price.currency = product_db.initial_currency

    voucher_code = product_dto.voucher_code # to do: check/setup Voucher code

    price.save(using='pricecheck_34')

    # back to view
    product_dto.initial_price = product_db.initial_price
    product_dto.product_max_count = MAX_PRODUCT_TRACKED
    product_dto.product_count = user.product_set.filter(tracked=True).count()
    product_dto.start_date = product_db.start_date.strftime('%d %B %Y, %H:%M')
    product_dto.end_date = product_db.end_date.strftime('%d %B %Y, %H:%M')
    product_dto.track_code = product_db.track_code
    product_dto.stop_code = product_db.stop_code
    product_dto.confirm_code = confirm_code
    product_dto.confirm_link = product_db.confirm_link
    product_dto.duration = str(product_db.duration) + ' day(s)'
    product_dto.threshold_up = product_dto.currency + str(product_db.threshold_up)
    product_dto.threshold_down = product_dto.currency + str(product_db.threshold_down)

    sub = 'Price Tracking Service: ' + product_dto.name
    templ = 'pricecheck/email_add_product.html'
    pricecheck.service_email.send_email(product_dto, sub, templ)

    return product_dto


def get_context_confirm(confirm_code):
    if Product.objects.using('pricecheck_34').filter(confirm_code=confirm_code).exists():
        product_db = Product.objects.using('pricecheck_34').get(confirm_code=confirm_code)
        product_db.confirmed = True
        product_db.save(using='pricecheck_34')
        product_dto = service_converters.convert_product_db2dto(product_db)
        context = {'product_dto': product_dto,
                   'success_info': SUCCESS_INFO,
                   'failure_info': FAILURE_INFO,
                   }
        ctx = {**service.get_base_context(), **context}
        print(product_db)
        print(context)
        return [True, ctx]
    else:
        context = {'failure_info': FAILURE_INFO}
        ctx = {**service.get_base_context(), **context}
        return [False, ctx]











