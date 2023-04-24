from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'temperatures', views.TemperatureViewSet)
router.register(r'light', views.LightViewSet)
router.register(r'humidity', views.HumidityViewSet)
router.register(r'temperatures', views.PirViewSet)
router.register(r'fan-state', views.FanViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth', include('rest_framework.urls')),
    path('post/', include('api.urls')),
]