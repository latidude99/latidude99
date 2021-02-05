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
from pricecheck.service_converters import *
import string, random


def update_prices(track_code):
    code = track_code.strip()
    if code != '' and len(code) < 16:# incorrect track_code
        error = code + ' - Invalid tracking code: the code has to be 16 characters long.'
        return error
    elif len(code) == 16: # correct track_code
        try:
            product = Product.objects.using('pricecheck_34').get(track_code=code)
            current_price = check_price(product,AMAZON_NAME_ID, AMAZON_PRICE_IDS)
            price = Price(product=product, price=current_price[1:], date=dt.datetime.utcnow().replace(tzinfo=pytz.UTC), currency=current_price[0])
            price.save(using='pricecheck_34')
            return code + ' product price updated.'
        except Product.DoesNotExist:
            error = code + ' - Invalid tracking code: no product found.'
            return error
    else: # update all by passing '' as track_code parameter
        products = Product.objects.using('pricecheck_34').filter(confirmed=True,tracked=True)
        for product in products:
            if product.confirmed:
                latest_price = product.price_set.latest('price')
                current_price = check_price(product, AMAZON_NAME_ID, AMAZON_PRICE_IDS)
                price = Price(product=product,
                              price=current_price[1:],
                              date=dt.datetime.utcnow().replace(tzinfo=pytz.UTC),
                              currency=current_price[0])
                price.save(using='pricecheck_34')
                product_dto = convert_product_db2dto(product)

                # if latest_price < current_price and current_price - latest_price >= product.threshold_down:
                #     send_email(product_dto)
                # elif latest_price > current_price and latest_price - current_price >= product.threshold_up:
                #     send_email(product_dto)
                sub = 'Price Tracking Service: ' + product_dto.name
                templ = 'pricecheck/email_check_product.html'
                pricecheck.service_email.send_email(product_dto, sub, templ)
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









