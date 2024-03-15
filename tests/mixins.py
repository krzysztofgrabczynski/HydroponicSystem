from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import random

from src.hydroponic_system.models import HydroponicSystem, Measurement, Sensors


class CreateUserForTestMixin:
    def setUp(self):
        self.credentials = {
            "username": "test_username",
            "password": "test_password123!",
        }

        self.test_user = User.objects.create_user(**self.credentials)


class LoginUserForTestMixin(CreateUserForTestMixin):
    def setUp(self):
        super().setUp()

        self.token = Token.objects.create(user=self.test_user)
        self.token_header = "Token " + self.token.key


def create_hydroponic_system(
    user: User,
    name: str = "test_name",
    description: str = "test_description",
    number_of_plants: int = 5,
) -> HydroponicSystem:
    return HydroponicSystem.objects.create(
        owner=user,
        name=name,
        description=description,
        number_of_plants=number_of_plants,
    )


def create_measurement(hydroponic_system: HydroponicSystem) -> Measurement:
    return Measurement.objects.create(
        system=hydroponic_system,
        sensor=random.choice(Sensors.values),
        value=random.randint(0, 100),
    )
