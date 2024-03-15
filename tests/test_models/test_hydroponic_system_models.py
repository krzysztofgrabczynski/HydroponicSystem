from django.test import TestCase

from src.hydroponic_system.models import HydroponicSystem
from tests.mixins import (
    CreateUserForTestMixin,
    create_hydroponic_system,
    create_measurement,
)


class TestHydroponicSystemModel(CreateUserForTestMixin, TestCase):
    def setUp(self):
        super().setUp()
        hydroponic_system = create_hydroponic_system(self.test_user)

        number_of_measurements = 15
        for _ in range(number_of_measurements):
            create_measurement(hydroponic_system)

    def test_get_measurement(self):
        limit = 5
        measurements = HydroponicSystem.objects.first().get_measurements(
            limit=limit
        )

        self.assertEqual(len(measurements), limit)
        self.assertGreater(measurements[0].date, measurements[limit - 1].date)
