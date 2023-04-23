from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.models import TemperatureSensor, FanState
# from rest_framework import permissions
from api.serializers import *


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def post(request):
    serializer = TemperatureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        if serializer['temperature'].value > 28.0:
            state = FanState.objects.get(pk=1)
            state.IsActive = True
            state.save()
        else:
            state = FanState.objects.get(pk=1)
            state.IsActive = False
            state.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = TemperatureSensor.objects.all().order_by('-time')
    serializer_class = TemperatureSerializer
    # permission_classes = [permissions.IsAuthenticated]


class FanViewSet(viewsets.ModelViewSet):
    queryset = FanState.objects.all()
    serializer_class = FanStateSerializer
