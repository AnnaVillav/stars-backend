
from django.contrib.auth import get_user_model, password_validation
from django.db import transaction
from rest_framework import serializers

from .models import Cliente


User = get_user_model()


class RegistroUsuarioSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"},
    )

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError(
                "Este nombre de usuario ya está registrado."
            )
        return value

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(
                "Este correo electrónico ya está registrado."
            )
        return value

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    @transaction.atomic
    def create(self, validated_data):
        usuario = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            is_staff=False,
            is_superuser=False,
        )

        Cliente.objects.create(usuario=usuario)

        return usuario
