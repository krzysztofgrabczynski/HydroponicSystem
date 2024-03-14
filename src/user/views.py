from rest_framework import generics, views, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from src.user.serializers import UserCreationSerializer, UserLoginSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    error_message = "Invalid credentials"

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)

        if user:
            token = self._create_user_auth_token(user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)

        return Response(
            {"error": self.error_message}, status=status.HTTP_401_UNAUTHORIZED
        )

    def _create_user_auth_token(self, user):
        token, _ = Token.objects.get_or_create(user=user)
        return token


class LogoutView(views.APIView):
    def post(self, request):
        self._delete_user_auth_token(request)
        return Response(status=status.HTTP_200_OK)

    def _delete_user_auth_token(self, request):
        Token.objects.filter(user=request.user).delete()
