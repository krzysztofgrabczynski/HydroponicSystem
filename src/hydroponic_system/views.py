from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from src.hydroponic_system.models import HydroponicSystem, Measurement
from src.hydroponic_system.serializers import (
    HydroponicSystemCreationSerializer,
    MeasurementSerializer,
    HydroponicSystemDetailSerializer,
    HydroponicSystemsListSerializer,
)


class HydroponicSystemViewSet(viewsets.ModelViewSet):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemCreationSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return HydroponicSystemDetailSerializer
        elif self.action == "list":
            return HydroponicSystemsListSerializer

        return self.serializer_class

    def get_queryset(self):
        queryset = HydroponicSystem.objects.filter(owner=self.request.user)
        return queryset


class PerformMeasurementView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [IsAuthenticated]
