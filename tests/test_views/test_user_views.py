from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse

from tests.mixins import CreateUserForTestMixin, LoginUserForTestMixin


class TestUserRegistration(TestCase):
    client = APIClient()

    def test_user_registration_with_valid_credentials(self):
        url = reverse("sign-up")
        data = {
            "username": "test_username",
            "password": "test_password123!",
            "password2": "test_password123!",
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)

    def test_user_registration_with_invalid_repassword(self):
        url = reverse("sign-up")
        data = {
            "username": "test_username",
            "password": "test_password123!",
            "password2": "test_password",
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(User.objects.count(), 0)


class TestUserLogin(CreateUserForTestMixin, TestCase):
    client = APIClient()

    def test_user_login_with_valid_credentials(self):
        url = reverse("login")
        data = {
            "username": self.credentials["username"],
            "password": self.credentials["password"],
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Token.objects.count(), 1)

        token = Token.objects.get(user=self.test_user)
        self.assertTrue(token.key)

    def test_user_login_with_invalid_credentials(self):
        url = reverse("login")
        data = {
            "username": "invalid_username",
            "password": "invalid_password",
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 401)


class TestUserLogout(LoginUserForTestMixin, TestCase):
    client = APIClient()

    def test_user_logout(self):
        self.assertEqual(Token.objects.count(), 1)

        url = reverse("logout")

        response = self.client.post(url, HTTP_AUTHORIZATION=self.token_header)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Token.objects.count(), 0)
