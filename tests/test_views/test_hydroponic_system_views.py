from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
import random

from tests.mixins import LoginUserForTestMixin, create_hydroponic_system
from src.hydroponic_system.models import HydroponicSystem, Sensors, Measurement


class TestHydroponicSystemViewSet(LoginUserForTestMixin, TestCase):
    client = APIClient()

    def test_create_hydroponic_system(self):
        url = reverse("hydroponic_system-list")
        data = {
            "owner": self.test_user,
            "name": "test_name",
            "description": "test description",
            "number_of_plants": 5,
        }

        response = self.client.post(
            url, data, HTTP_AUTHORIZATION=self.token_header
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(HydroponicSystem.objects.count(), 1)

    def test_list_hydroponic_system(self):
        number_of_systems = 3
        for i in range(number_of_systems):
            name = f"test_name_{i + 1}"
            create_hydroponic_system(user=self.test_user, name=name)

        url = reverse("hydroponic_system-list")

        response = self.client.get(url, HTTP_AUTHORIZATION=self.token_header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(HydroponicSystem.objects.count(), number_of_systems)

    def test_detail_hydroponic_system(self):
        hydroponic_system = create_hydroponic_system(user=self.test_user)

        url = reverse("hydroponic_system-detail", args=[hydroponic_system.pk])

        response = self.client.get(url, HTTP_AUTHORIZATION=self.token_header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(HydroponicSystem.objects.count(), 1)

    def test_update_hydroponic_system(self):
        hydroponic_system = create_hydroponic_system(user=self.test_user)

        url = reverse("hydroponic_system-detail", args=[hydroponic_system.pk])
        date = {
            "name": hydroponic_system.name,
            "description": hydroponic_system.description,
            "number_of_plants": hydroponic_system.number_of_plants + 1,
        }

        response = self.client.put(
            url,
            date,
            content_type="application/json",
            HTTP_AUTHORIZATION=self.token_header,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(HydroponicSystem.objects.count(), 1)

    def test_delete_hydroponic_system(self):
        hydroponic_system = create_hydroponic_system(user=self.test_user)

        url = reverse("hydroponic_system-detail", args=[hydroponic_system.pk])

        response = self.client.delete(
            url, HTTP_AUTHORIZATION=self.token_header
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(HydroponicSystem.objects.count(), 0)


class TestMeasurement(LoginUserForTestMixin, TestCase):
    def test_measurement(self):
        hydroponic_system = create_hydroponic_system(user=self.test_user)

        url = reverse("measurement")
        date = {
            "system": hydroponic_system.pk,
            "sensor": random.choice(Sensors.values),
            "value": random.randint(0, 100),
        }

        response = self.client.post(
            url, date, HTTP_AUTHORIZATION=self.token_header
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Measurement.objects.count(), 1)
