from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=5000)
    date = models.DateTimeField('date')
    ip = models.CharField(max_length=200)
    sent = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    app_name = models.CharField(max_length=100)

    def __str__(self):
        return self.app_name + self.email + self.subject