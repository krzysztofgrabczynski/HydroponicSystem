from django.test import TestCase
from django.contrib.auth.models import User
import random

from src.hydroponic_system.models import HydroponicSystem, Measurement, Sensors


class TestHydroponicSystemModel(TestCase):
    def setUp(self):
        self._create_hydroponic_system()
        self._create_measurements(number_of_measurements=15)

    def test_get_measurement(self):
        limit = 5
        measurements = HydroponicSystem.objects.first().get_measurements(
            limit=limit
        )

        self.assertEqual(len(measurements), limit)
        self.assertGreater(measurements[0].date, measurements[limit - 1].date)

    def _create_hydroponic_system(self) -> None:
        HydroponicSystem.objects.create(
            owner=User.objects.create_user(username="test_username"),
            name="test_name",
            description="test_description",
            number_of_plants=5,
        )

    def _create_measurements(self, number_of_measurements: int) -> None:
        for _ in range(number_of_measurements):
            Measurement.objects.create(
                system=HydroponicSystem.objects.first(),
                sensor=random.choice(Sensors.values),
                value=random.randint(0, 100),
            )
