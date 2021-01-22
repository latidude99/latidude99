from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    start_date = models.DateTimeField()
    registered = models.BooleanField(default=False)
    registration_date =  models.DateTimeField()
    active = models.BooleanField(default=True)
    suspended = models.BooleanField(default=False)
    credit = models.IntegerField(default=0)

    def __str__(self):
        return self.email


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=2000)
    name = models.CharField(max_length=500)
    initial_date = models.DateTimeField('date')
    initial_price = models.FloatField(default=0)
    validated = models.BooleanField(default=False)
    traced = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField()
    price = models.FloatField(default=0)
    available = models.BooleanField(default=False)

    def __str__(self):
        return str(self.price) + " - " + str(self.date)












