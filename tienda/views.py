from django.shortcuts import render
from rest_framework import viewsets

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


# Vista principal de bienvenida (BACK-008)
def bienvenida(request):
    return render(request, "tienda/bienvenida.html")


# ViewSets de la API REST (BACK-010)
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ProductoDetalleSerializer
        return ProductoSerializer


class ImagenProductoViewSet(viewsets.ModelViewSet):
    queryset = ImagenProducto.objects.all()
    serializer_class = ImagenProductoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PedidoDetalleSerializer
        return PedidoSerializer


class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer


class EnvioViewSet(viewsets.ModelViewSet):
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer