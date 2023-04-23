import datetime

from django.db import models


# Create your models here.
class TemperatureSensor(models.Model):
    temperature = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
