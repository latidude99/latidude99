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



def get_product_info(product_dto, flag):
    code = ''
    prices = ''
    product_db = ''
    if flag  == 'track' and len(product_dto.track_code) != 16:
        product_dto.error1 = product_dto.track_code + '  Invalid tracking code: it has to be exactly 16 characters long.'
        return [product_dto, prices]
    elif flag  == 'stop' and len(product_dto.stop_code) != 16:
        product_dto.error2 = product_dto.stop_code + '  Invalid stop code: it has to be exactly 16 characters long.'
        return [product_dto, prices]

    try:
        if flag  == 'stop':
            code = product_dto.stop_code.strip()
            product_db = Product.objects.using('pricecheck_34').get(stop_code=code)
            product_db.tracked = False
            product_db.save(using='pricecheck_34')
        elif flag  == 'track':
            code = product_dto.track_code.strip()
            product_db = Product.objects.using('pricecheck_34').get(track_code=code)

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
        product_dto.duration = str(product_db.duration) + ' day(s)'
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








