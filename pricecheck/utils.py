#import django
#django.setup()

from pricecheck.models import *


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


# ------------------------------------------------------------------

#delete_all_users()















