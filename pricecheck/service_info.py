# import django
# django.setup()

from pricecheck.models import *
import requests
from bs4 import BeautifulSoup
import pricecheck.service_email
import pricecheck.service as service
import pricecheck.service_add as service_add
import pricecheck.service_track as service_track
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
from lxml.html import fromstring
from itertools import cycle
import traceback


def get_product_info_context(product_dto, flag):
    info = get_product_info(product_dto, flag)
    context = {'product_dto': info[0],
               'prices': info[1],

               }
    ctx = {**service.get_base_context(), **service.get_index_context(), **context}
    return ctx


def get_product_info(product_dto, flag):
    code = ''
    prices = ''
    product_db = ''
    if flag == 'track' and len(product_dto.track_code) != 16:
        product_dto.error1 = product_dto.track_code + '  Invalid tracking code: it has to be exactly 16 characters long.'
        return [product_dto, prices]
    elif flag == 'stop' and len(product_dto.stop_code) != 16:
        product_dto.error2 = product_dto.stop_code + '  Invalid stop code: it has to be exactly 16 characters long.'
        return [product_dto, prices]

    try:
        if flag == 'stop':
            code = product_dto.stop_code.strip()
            product_db = Product.objects.using('pricecheck_34').get(stop_code=code)
            product_db.tracked = False
            product_db.save(using='pricecheck_34')

        elif flag == 'track':
            print('flag = track')
            code = product_dto.track_code.strip()
            product_db = Product.objects.using('pricecheck_34').get(track_code=code)

        if product_db == '':
            product_dto.error1 = 'An error occurred while connecting to database.'
            return [product_dto, prices]

        user = product_db.user
        product_dto.username = user.name
        product_dto.email = user.email
        product_dto.product_max_count = user.max_items_tracked
        product_dto.product_count = user.product_set.filter(tracked=True).count()
        product_dto.name = product_db.name
        product_dto.initial_price = product_db.initial_price
        product_dto.currency = product_db.initial_currency

        product_dto.start_date = product_db.start_date.strftime('%d %B %Y, %H:%M')
        product_dto.end_date = product_db.end_date.strftime('%d %B %Y, %H:%M')
        timedelta = product_db.end_date - dt.datetime.utcnow().replace(tzinfo=pytz.UTC)
        if product_db.tracked:
            product_dto.duration_left = str(timedelta.days)
        else:
            product_dto.duration_left = '0'
        prices = product_db.price_set.all()
        price_labels = [x.date.strftime('%d %b %Y, %H:%M') for x in prices]
        price_values = [x.price for x in prices]
        product_dto.current_price = price_values[-1]

        product_dto.price_diff = product_dto.initial_price - product_dto.current_price

        labels_filler = ['waiting'] * (timedelta.days * 3)
        values_filler = [0] * (timedelta.days * 3)
        product_dto.price_labels = price_labels + labels_filler
        product_dto.price_values = price_values + values_filler

        product_dto.track_code = product_db.track_code
        product_dto.stop_code = product_db.stop_code
        if product_db.duration == 1:
            product_dto.duration = str(product_db.duration) + ' day'
        else:
            product_db.duration = str(product_db.duration) + ' days'
        product_dto.threshold_up = product_dto.currency + str(product_db.threshold_up)
        product_dto.threshold_down = product_dto.currency + str(product_db.threshold_down)

        if product_db.tracked:
            product_dto.status = 'Tracked'
        else:
            product_dto.status = 'Not tracked'

    except Product.DoesNotExist:
        product_dto.error = ' - Invalid code: no product found.'
        product_dto.code = code
        return [product_dto, prices]

    return [product_dto, prices]


def get_product_list_context(email, user_id):
    info = get_product_list(email, user_id)
    context = {'status': info[0],
               'error_msg': info[1],
               'products': info[2],
               'user': info[3]
               }
    print(info)
    ctx = {**service.get_base_context(), **service.get_index_context(), **context}
    return ctx


def get_product_list(email, user_id):
    dto_list = []
    if User.objects.using('pricecheck_34').filter(email=email, unique_id=user_id).exists():
        user = User.objects.using('pricecheck_34').get(email=email, unique_id=user_id)
        products = Product.objects.using('pricecheck_34').filter(user=user)

        for product in products:
            dto = convert_product_db2dto(product)
            if product.tracked:
                dto.status = 'tracked'
            else:
                dto.status = 'stopped or expired'
            dto_list.append(dto)

        dto_list.sort(key=lambda x: x.status, reverse=True)
        return [True, None, dto_list, user]
    else:
       error= 'The email address and the unique user id do not match'
    return [False, error, None, None]












