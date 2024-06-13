from rest_framework import viewsets
from .models import Equipment, Data, Alerts
from .serializers import EquipmentSerializer, DataSerializer, AlertsSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class AlertsViewSet(viewsets.ModelViewSet):
    queryset = Alerts.objects.all()
    serializer_class = AlertsSerializer
