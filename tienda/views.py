from django.shortcuts import render
from rest_framework import viewsets
from django.db.models import F
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser

from .models import (
    Categoria,
    Marca,
    Proveedor,
    Producto,
    ImagenProducto,
    Cliente,
    Pedido,
    DetallePedido,
    Pago,
    Envio,
)

from .serializers import (
    CategoriaSerializer,
    MarcaSerializer,
    ProveedorSerializer,
    ProductoSerializer,
    ProductoDetalleSerializer,
    ImagenProductoSerializer,
    ClienteSerializer,
    PedidoSerializer,
    PedidoDetalleSerializer,
    DetallePedidoSerializer,
    PagoSerializer,
    EnvioSerializer,
)

class LecturaPublicaEscrituraAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )

def bienvenida(request):
    return render(request, "tienda/bienvenida.html")


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [LecturaPublicaEscrituraAdmin]


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [LecturaPublicaEscrituraAdmin]


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAdminUser]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [LecturaPublicaEscrituraAdmin]

    filterset_fields = ["categoria", "marca", "activo"]
    search_fields = ["nombre", "descripcion"]
    ordering_fields = ["precio", "stock", "nombre"]
    ordering = ["nombre"]

    def get_serializer_class(self):
        if self.action in ["list", "ofertas", "bajo_stock"]:
            return ProductoDetalleSerializer
        return ProductoSerializer

    @action(detail=False, methods=["get"], url_path="ofertas")
    def ofertas(self, request):
        productos = self.get_queryset().filter(
            activo=True,
            precio_oferta__isnull=False,
            precio_oferta__lt=F("precio")
        )
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="bajo-stock")
    def bajo_stock(self, request):
        productos = self.get_queryset().filter(
            activo=True,
            stock__lte=5
        )
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)


class ImagenProductoViewSet(viewsets.ModelViewSet):
    queryset = ImagenProducto.objects.all()
    serializer_class = ImagenProductoSerializer
    permission_classes = [LecturaPublicaEscrituraAdmin]


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAdminUser]
    



class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action == "list":
            return PedidoDetalleSerializer
        return PedidoSerializer


class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    permission_classes = [IsAdminUser]


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAdminUser]


class EnvioViewSet(viewsets.ModelViewSet):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer
    permission_classes = [IsAdminUser]