# import django
# django.setup()

from pricecheck.models import *
import requests
from bs4 import BeautifulSoup
import pricecheck.service_email as service_email
import latidude99.settings as settings
import datetime as dt
import pytz
from django.utils import timezone
from pricecheck.text import *
from pricecheck.models import *
from pricecheck.dto import *
from pricecheck.service_converters import *
from pricecheck.const import *
import string, random
import pricecheck.service_proxy as service_proxy

def update_prices(track_code):
    code = track_code.strip()
    if code != '' and len(code) < 16:  # incorrect track_code
        error = code + ' - Invalid tracking code: the code has to be 16 characters long.'
        return error
    elif len(code) == 16:  # correct track_code, no emails
        try:
            product = Product.objects.using('pricecheck_34').get(track_code=code)
            current_price = check_price(product)
            price = Price(product=product, price=current_price[1:], date=dt.datetime.utcnow().replace(tzinfo=pytz.UTC),
                          currency=current_price[0])
            price.save(using='pricecheck_34')
            return code + ' product price updated.'
        except Product.DoesNotExist:
            error = code + ' - Invalid tracking code: no product found.'
            return error
    else:  # update all by passing '' as track_code parameter and send out emails
        products = Product.objects.using('pricecheck_34').filter(confirmed=True, tracked=True)
        for product in products:
            if product.confirmed:
                timedelta = product.end_date - dt.datetime.utcnow().replace(tzinfo=pytz.UTC)
                if timedelta.days < 0:
                    product.tracked = False
                    product.save(using='pricecheck_34')
                    continue
                prices = product.price_set.all()
                price_values = [x.price for x in prices]
                initial_price = price_values[0]
                latest_price = price_values[-1]
                current_price = check_price(product)
                price = Price(product=product,
                              price=current_price[1:],
                              date=dt.datetime.utcnow().replace(tzinfo=pytz.UTC),
                              currency=current_price[0])
                price.save(using='pricecheck_34')
                product = Product.objects.using('pricecheck_34').get(track_code=product.track_code)
                product_dto = convert_product_db2dto(product)
                product_dto.track_link = APP_BASE + '/product?track_code=' + product.track_code
                product_dto.stop_link = APP_BASE + '/product?stop_code=' + product.stop_code
                product_dto.app_link = APP_BASE

                sub = 'Price Tracking Service: ' + product_dto.name
                templ = 'pricecheck/email_check_product.html'

                curr_price_float = float(current_price[1:].replace(',', ''))

                if latest_price < curr_price_float and curr_price_float - latest_price >= product.threshold_down:
                    product_dto.price_diff = curr_price_float - latest_price
                    service_email.send_email(product_dto, sub, templ)
                    print('threshold_down')
                    print('current_price')
                    print(curr_price_float)
                elif latest_price > curr_price_float and latest_price - curr_price_float >= product.threshold_up:
                    product_dto.price_diff = curr_price_float - latest_price
                    service_email.send_email(product_dto, sub, templ)
                    print('threshold_up')
                    print('current_price')
                    print(curr_price_float)

                # sub = 'Price Tracking Service: ' + product_dto.name
                # templ = 'pricecheck/email_check_product.html'
                # service_email.send_email(product_dto, sub, templ)

                print('price updated for: ' + product.name)
        return str(len(products)) + ' products prices updated.'




def check_price(product):
    price = ''
    response = get_response(product.url)
    if LEWIS_WEBSITE in product.url:
        price = get_price_lewis(response)
    elif AMAZON_WEBSITE in product.url:
        price = get_price_amazon(response)
    return price


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


def get_price_amazon(response):
    div_price = None
    soup = BeautifulSoup(response.content, 'html.parser')
    div_price = soup.find(id=AMAZON_PRICE_IDS[1])
    price = ''
    if div_price != None:
        price = div_price.get_text().strip()
    return price


def get_price_lewis(response):
    div_price = None
    soup = BeautifulSoup(response.content, 'html.parser')
    div_price = soup.find_all('span', {'class': LEWIS_PRICE_CLASS})
    print(div_price[0].text)
    price = ''
    if div_price != None:
        price = (div_price[0].text)
    return price


# not used for the moment
def check_price_tags(product, price_tags):
    product_price = ''

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(product.url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(page.content, 'html.parser')
    div_price = None
    for id in price_tags:
        div_price = soup.find(id=id)
        if div_price != None:  # found the working price tag
            break
    if div_price != None:
        product_price = div_price.get_text().strip()
    return product_price


# not used for the moment
def check_price_proxy(product, price_tags):
    product_price = ''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

    proxies_pool = service_proxy.get_proxies_1(PROXY_POOL)
    print('proxies_pool: ' + str(len(proxies_pool)))
    div_price = None
    proxies_num = len(proxies_pool)
    count = 0
    while count < proxies_num:
        count = count + 1
        try:
            proxy = random.choice(proxies_pool)
            proxy_dict = {
                'http': proxy,
                'https': proxy
            }
            print("trying with:", proxy_dict)
            response = requests.get(product.url,
                                    headers=headers,
                                 #   proxies=proxy_dict,
                                    timeout=7)

            soup = BeautifulSoup(response.content, 'html.parser')
            for id in price_tags:
                div_price = soup.find(id=id)
                if div_price != None:  # found the working price tag
                    break
            break
        except:
            print("Connection error, looking for another proxy")
            pass

    if div_price != None:
        product_price = div_price.get_text().strip()

    return product_price
