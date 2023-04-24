from django.db import models


# Create your models here.
class TemperatureSensor(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    time = models.DateTimeField(auto_now_add=True, blank=True)


class LightSensor(models.Model):
    lightValue = models.SmallIntegerField()
    time = models.DateTimeField(auto_now_add=True, blank=True)


class HumiditySensor(models.Model):
    humidityValue = models.SmallIntegerField()
    time = models.DateTimeField(auto_now_add=True, blank=True)


class PirSensor(models.Model):
    pirState = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True, blank=True)


class FanState(models.Model):
    IsActive = models.SmallIntegerField()
    time = models.DateTimeField(auto_now_add=True, blank=True)
