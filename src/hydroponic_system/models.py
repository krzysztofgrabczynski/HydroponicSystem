from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class HydroponicSystem(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hydroponic_system_model"
    )
    name = models.CharField()
    description = models.TextField()
    number_of_plants = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.name} Hydroponic System"

    def get_measurements(self, limit: int = 10) -> list:
        return self.measurement_model.all().order_by("-date")[:limit]


class Sensors(models.IntegerChoices):
    pH = 0
    water_temperature = 1
    TDS = 2


class Measurement(models.Model):
    system = models.ForeignKey(
        HydroponicSystem,
        on_delete=models.CASCADE,
        related_name="measurement_model",
    )
    sensor = models.PositiveSmallIntegerField(choices=Sensors.choices)
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Measurement value of the {self.system} - using {self.sensor} sensor: {self.value}"
