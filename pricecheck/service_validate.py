#import django
#django.setup()

from pricecheck.models import *
import requests
from bs4 import BeautifulSoup
from random import choice
import html5lib

from lxml.html import fromstring
from itertools import cycle
import traceback

import pricecheck.service_email
import pricecheck.service as service
import pricecheck.service_proxy as service_proxy
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
import string, random


def validate_url(url, product_id, price_ids):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

    proxies_pool = service_proxy.get_proxies_1(PROXY_POOL)
    print('proxies_pool: ' + str(len(proxies_pool)))
    div_price = None
    div_product = None
    proxies_num = len(proxies_pool)
    count = 0
    while count < proxies_num:
        count = count + 1
        try:
            proxy = choice(proxies_pool)
            proxy_dict = {
                'http': proxy,
                'https': proxy
            }
            print("trying with:", proxy_dict)
            response = requests.get(url,
                                    headers=headers,
                                 #   proxies=proxy_dict,
                                    timeout=7)

           # print(response.json())
            soup = BeautifulSoup(response.content, 'html.parser')
            div_product = soup.find(id=product_id)

            for id in price_ids:
                div_price = soup.find(id=id)
                if div_price != None:  # found the working price tag
                    break
           # print(response.text)
            print(url)
            print(product_id)
            print(price_ids)
            print(div_price)
            break
        except:
            print("Connection error, looking for another proxy")
            pass

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




#--------------------------------------------------------------------------------------------

#response = data_scraper('get', "https://zenscrape.com/ultimate-list-15-best-services-offering-rotating-proxies/")
#print(response.text)

# url_test = 'https://httpbin.org/ip'
# url_yes = 'https://www.amazon.co.uk/Motorola-zero-notch-display-Qualcomm-Snapdragon/dp/B0846HGNNB/ref=sr_1_3?dchild=1&keywords=moto+g8+power&qid=1612974757&s=electronics&sr=1-3'
# url_no ='https://www.amazon.co.uk/Motorola-display-octa-core-processor-battery/dp/B085J9DBVH/ref=sr_1_6?dchild=1&keywords=moto+g8+power&qid=1612974757&s=electronics&sr=1-6'
# validate_url(url_no, AMAZON_NAME_ID, AMAZON_PRICE_IDS)

#--------------------------------------------------------------------------------------------
