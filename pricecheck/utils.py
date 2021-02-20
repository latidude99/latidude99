#import django
#django.setup()


import logging
import threading
import time
import datetime as dt
import pytz
from pricecheck.models import *
import pricecheck.service as service
import pricecheck.service_info as service_info
import pricecheck.service_add as service_add
import pricecheck.service_track as service_track


def set_missing_unique_id_for_users():
    users = User.objects.using('pricecheck_34').all()
    for user in users:
        if len(user.unique_id) < 32:
            unique_id = service.get_random_string(32)
            while User.objects.using('pricecheck_34').filter(unique_id=unique_id).exists():
                unique_id = service.get_random_string(32)
            user.unique_id = unique_id
            print('unique_id set for ' + user.email + ', ' + user.unique_id)
        user.save(using='pricecheck_34')


# set_missing_unique_id_for_users()



def delete_all_users():
    User.objects.using('pricecheck_34').all().delete()
    print('all users deleted')


def delete_all_vouchers():
    Voucher.objects.using('pricecheck_34').all().delete()
    print('all vouchers deleted')


def delete_all_products():
    Product.objects.using('pricecheck_34').all().delete()
    print('all products deleted')


def delete_all_prices():
    Price.objects.using('pricecheck_34').all().delete()
    print('all prices deleted')


def set_limit_for_user(email, limit):
    if User.objects.using('pricecheck_34').filter(email=email).exists():
        user = User.objects.using('pricecheck_34').get(email=email)
        user.max_items_tracked = limit
        user.save(using='pricecheck_34')
        print('new limit of ' + str(limit) + ' products set for user ' + email)
    else:
        print('user ' + email + ' not found')


def delete_all_products_for_user(email):
    if User.objects.using('pricecheck_34').filter(email=email).exists():
        user = User.objects.using('pricecheck_34').get(email=email)
        user.product_set.all().delete()
        print('all products deleted')


def worker(arg):
    while not arg["stop"]:
        logging.debug("worker thread checking in")
        service_track.update_prices('')
        print(dt.datetime.utcnow().replace(tzinfo=pytz.UTC))
        time.sleep(1)

def constant_product_update_intervals_and_max_munber(interval, max): # interval in sec
    count = 0
    while max > count:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(relativeCreated)6d %(threadName)s %(message)s"
        )
        info = {"stop": False}
        thread = threading.Thread(target=worker, args=(info,))
        thread.start()
        # while True:
        #     try:
        #         logging.debug("Checking in from main thread")
        #         time.sleep(0.75)
        #     except KeyboardInterrupt:
        #         info["stop"] = True
        #         logging.debug('Stopping')
        #         break
        thread.join()
        count = count + 1
        print('count= ' + str(count))
        time.sleep(interval)




# ------------------------------------------------------------------

#delete_all_users()


#print(update_prices(''))


#set_limit_for_user('latidude99test@gmail.com', 50)
#set_limit_for_user('latidude99@gmail.com', 50)

#delete_all_products_for_user('latidude99test@gmail.com')
#delete_all_products_for_user('latidude99@gmail.com')



#constant_product_update_intervals_and_max_munber(interval=15,max=5)





