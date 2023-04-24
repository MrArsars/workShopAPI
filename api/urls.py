from django.urls import include, path

from api.views import *

urlpatterns = [
    path('temperature', TemperaturePost),
    path('light', LightPost),
    path('humidity', HumidityPost),
    path('pir', PirPost),
]
