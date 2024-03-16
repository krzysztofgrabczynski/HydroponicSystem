from rest_framework import serializers

from src.hydroponic_system.models import HydroponicSystem, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["system", "sensor", "value", "date"]
        extra_kwargs = {"date": {"read_only": True}}


class HydroponicSystemCreationSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = HydroponicSystem
        fields = ["owner", "name", "description", "number_of_plants"]


class HydroponicSystemDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieve user Hydroponic System with information about the measurements taken.
    """

    measurements = serializers.SerializerMethodField()

    class Meta:
        model = HydroponicSystem
        fields = [
            "id",
            "owner",
            "name",
            "description",
            "number_of_plants",
            "measurements",
        ]

    def get_measurements(self, hydroponic_system: HydroponicSystem) -> list:
        measurements = hydroponic_system.get_measurements()
        serializer = MeasurementSerializer(measurements, many=True)
        return serializer.data


class HydroponicSystemsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HydroponicSystem
        fields = ["id", "name"]
