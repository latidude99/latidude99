from django.db import models
from django.utils import timezone

from pricecheck.const import *


class User(models.Model):
    name = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, unique=True, default='')
    password = models.CharField(max_length=32, default='')
    unique_id = models.CharField(max_length=32, default='')
    registered = models.BooleanField(default=False)
    registration_date =  models.DateTimeField(default=timezone.now, blank=True)
    active = models.BooleanField(default=True)
    suspended = models.BooleanField(default=False)
    credit = models.IntegerField(default=0)
    emails_sent = models.IntegerField(default=0)
    max_items_tracked = models.IntegerField(default=MAX_PRODUCT_TRACKED)

    def __str__(self):
        return self.email


class Voucher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, default='')
    issued = models.DateTimeField(default=timezone.now, blank=True)
    expired = models.BooleanField(default=False)
    credit = models.IntegerField(default=0)



class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=2000, default='')
    name = models.CharField(max_length=500, default='')
    start_date = models.DateTimeField(default=timezone.now, blank=True)
    end_date = models.DateTimeField(default=timezone.now, blank=True)
    duration = models.IntegerField(default=0) # days
    initial_price = models.FloatField(default=0)
    initial_currency = models.CharField(max_length=50, default='')
    validated = models.BooleanField(default=False)
    tracked = models.BooleanField(default=False)
    track_code = models.CharField(max_length=50, default='')
    stop_code = models.CharField(max_length=50, default='')
    threshold_up = models.FloatField(default=0.01)
    threshold_down = models.FloatField(default=0.01)
    confirm_link = models.CharField(max_length=200, default='')
    confirm_code = models.CharField(max_length=50, default='')
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, blank=True)
    price = models.FloatField(default=0)
    currency = models.CharField(max_length=50, default='')

    def __str__(self):
        return str(self.price) + " - " + str(self.date)




#dt.timedelta(days=int(product_dto.duration))







