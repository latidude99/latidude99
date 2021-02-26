# import django
# django.setup()

from pricecheck.models import *
import requests
import requests_html as requests_html  # import HTMLSession
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


def validate_url(url):
    validation = ''
    response = get_response(url)
    if LEWIS_WEBSITE in url:
        validation = validate_lewis(response, LEWIS_NAME_CLASS, LEWIS_PRICE_CLASS)
    elif AMAZON_WEBSITE in url:
        validation = validate_amazon(response, AMAZON_NAME_ID, AMAZON_PRICE_IDS[1])

    return validation


def get_response(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69"}
    response = ''
    try:
        print("trying with:", proxies)
        response = requests.get(url,
                                headers=headers,
                                #  proxies=proxies,
                                timeout=15)
    except:
        print("Connection error")
        pass
    return response


def validate_amazon(response, name, price):
    div_price = None
    div_product = None
    soup = BeautifulSoup(response.content, 'html.parser')
    print('search amazon')
    div_product = soup.find(id=name)
    div_price = soup.find(id=price)
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


def validate_lewis(response, name, price):
    div_price = None
    div_product = None
    soup = BeautifulSoup(response.content, 'html.parser')
    print('search by class')
    div_product = soup.find_all('h1', {'class': name})
    div_price = soup.find_all('span', {'class': price})

    print(div_product[0].text)
    print(div_price[0].text)

    validation = {}
    if div_price != None:
        product_name = div_product[0].text
        product_price = (div_price[0].text)
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


def get_response_2(url):
    response = ''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69"}

    proxies_pool = service_proxy.get_proxies_1(PROXY_POOL)
    print('proxies_pool: ' + str(len(proxies_pool)))

    proxies_num = len(proxies_pool)
    count = 0
    while count < 15:  # proxies_num:
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
                                    proxies=proxy_dict,
                                    timeout=15)
            break
        except:
            print("Connection error, looking for another proxy")
            pass
    return response


# uses requests-html
def validate_url_3(url, product_id, price_id):
    # headers = {
    #    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    div_price = None
    div_product = None
    try:
        session = requests_html.HTMLSession()
        response = session.get(url)

        div_price = response.html.find('#id', first=True).text
        div_product = response.html.find('#product_id', first=True).text
        print(div_price)
        print(product_id)
    except requests.exceptions.RequestException as e:
        print(e)

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

# --------------------------------------------------------------------------------------------

# response = data_scraper('get', "https://zenscrape.com/ultimate-list-15-best-services-offering-rotating-proxies/")
# print(response.text)

# url_test = 'https://httpbin.org/ip'
# url_yes = 'https://www.amazon.co.uk/Motorola-zero-notch-display-Qualcomm-Snapdragon/dp/B0846HGNNB/ref=sr_1_3?dchild=1&keywords=moto+g8+power&qid=1612974757&s=electronics&sr=1-3'
# url_no ='https://www.amazon.co.uk/Motorola-display-octa-core-processor-battery/dp/B085J9DBVH/ref=sr_1_6?dchild=1&keywords=moto+g8+power&qid=1612974757&s=electronics&sr=1-6'
# validate_url(url_no, AMAZON_NAME_ID, AMAZON_PRICE_IDS)

# --------------------------------------------------------------------------------------------
