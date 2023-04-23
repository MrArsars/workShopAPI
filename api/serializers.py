from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import TemperatureSensor


class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TemperatureSensor
        fields = ['temperature', 'time']
