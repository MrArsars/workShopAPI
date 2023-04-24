from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import *


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemperatureSensor
        fields = ['temperature', 'humidity', 'time']


class LightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LightSensor
        fields = ['lightValue', 'time']


class HumiditySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HumiditySensor
        fields = ['humidityValue', 'time']


class PirSerializer(serializers.HyperlinkedModelSerializer):
    model = PirSensor
    fields = ['pirState', 'time']


class FanStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FanState
        fields = ['IsActive']
