
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from .registro_serializers import RegistroUsuarioSerializer


class RegistroThrottle(AnonRateThrottle):
    rate = "5/hour"


class RegistroUsuarioView(CreateAPIView):
    serializer_class = RegistroUsuarioSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
    throttle_classes = [RegistroThrottle]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = serializer.save()

        return Response(
            {
                "mensaje": "Cuenta creada correctamente.",
                "username": usuario.username,
            },
            status=status.HTTP_201_CREATED,
        )
