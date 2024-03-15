from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


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
