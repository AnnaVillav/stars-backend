
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UsuarioActualView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        usuario = request.user

        return Response({
            "id": usuario.id,
            "username": usuario.username,
            "email": usuario.email,
            "is_staff": usuario.is_staff,
            "is_superuser": usuario.is_superuser,
        })
