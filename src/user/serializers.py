from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserCreateMixin:
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user


class UserCreationSerializer(UserCreateMixin, serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]
        extra_kwargs = {
            "password": {
                "write_only": True,
                "validators": [validate_password],
            },
        }

    def validate(self, attrs):
        if not attrs["password"] == attrs.pop("password2"):
            error_message = {"password": "Password fields must be the same"}
            raise serializers.ValidationError(error_message)

        return super().validate(attrs)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
