import django
django.setup()

from pricecheck.models import *
from pricecheck.service_track import *


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

# ------------------------------------------------------------------

#delete_all_users()


#print(update_prices(''))


#set_limit_for_user('latidude99test@gmail.com', 50)
#set_limit_for_user('latidude99@gmail.com', 50)

#delete_all_products_for_user('latidude99test@gmail.com')
#delete_all_products_for_user('latidude99@gmail.com')









