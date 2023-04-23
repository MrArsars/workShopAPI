from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import TemperatureSensor, FanState


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemperatureSensor
        fields = ['temperature', 'time']


class FanStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FanState
        fields = ['IsActive']
