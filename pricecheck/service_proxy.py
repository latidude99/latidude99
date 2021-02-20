#import django
#django.setup()

import requests
from bs4 import BeautifulSoup
from random import choice






# scrape proxies from free-proxy-list.net
def get_proxies_1(proxies_pool):
    response = requests.get(proxies_pool)
    soup = BeautifulSoup(response.content, 'html5lib')
    proxies = list(map(lambda x: x[0] + ':' + x[1], list(zip(map(lambda x: x.text, soup.findAll('td')[::8]),
                                                       map(lambda x: x.text, soup.findAll('td')[1::8])))))
    #proxy = {'https': choice(proxies)}
    return proxies

