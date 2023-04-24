from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.models import *
# from rest_framework import permissions
from api.serializers import *


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def TemperaturePost(request):
    serializer = TemperatureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        if serializer['temperature'].value > 23.0:
            state = FanState.objects.get(pk=1)
            state.IsActive = 255
            state.save()
        else:
            state = FanState.objects.get(pk=1)
            state.IsActive = 0
            state.save()
        print("TEMPERATURE AND HUM:", serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def LightPost(request):
    serializer = LightSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("LIGHT:", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def HumidityPost(request):
    serializer = HumiditySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("HUMIDITY:", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def PirPost(request):
    serializer = PirSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("PIR:", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = TemperatureSensor.objects.all().order_by('-time')
    serializer_class = TemperatureSerializer
    # permission_classes = [permissions.IsAuthenticated]


class LightViewSet(viewsets.ModelViewSet):
    queryset = LightSensor.objects.all().order_by('-time')
    serializer_class = LightSerializer
    # permission_classes = [permissions.IsAuthenticated]


class HumidityViewSet(viewsets.ModelViewSet):
    queryset = HumiditySensor.objects.all().order_by('-time')
    serializer_class = HumiditySerializer
    # permission_classes = [permissions.IsAuthenticated]


class PirViewSet(viewsets.ModelViewSet):
    queryset = PirSensor.objects.all().order_by('-time')
    serializer_class = PirSerializer
    # permission_classes = [permissions.IsAuthenticated]


class FanViewSet(viewsets.ModelViewSet):
    queryset = FanState.objects.all()
    serializer_class = FanStateSerializer
    permission_classes = [permissions.IsAuthenticated]
