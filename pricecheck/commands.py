#import django
#django.setup()

from pricecheck.models import *
import pricecheck.service as service
import pricecheck.service_info as service_info
import pricecheck.service_add as service_add
import pricecheck.service_track as service_track


def update_all_products():
    service_track.update_prices('') # '' = all products
    print('Price update finished')












