from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tienda.views import (
    bienvenida,
    CategoriaViewSet,
    MarcaViewSet,
    ProveedorViewSet,
    ProductoViewSet,
    ImagenProductoViewSet,
    ClienteViewSet,
    PedidoViewSet,
    DetallePedidoViewSet,
    PagoViewSet,
    EnvioViewSet,
)

router = DefaultRouter()

router.register(r"categorias", CategoriaViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"proveedores", ProveedorViewSet)
router.register(r"productos", ProductoViewSet)
router.register(r"imagenes-producto", ImagenProductoViewSet)
router.register(r"clientes", ClienteViewSet)
router.register(r"pedidos", PedidoViewSet)
router.register(r"detalles-pedido", DetallePedidoViewSet)
router.register(r"pagos", PagoViewSet)
router.register(r"envios", EnvioViewSet)


urlpatterns = [
    path("", bienvenida, name="inicio"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]