from django.contrib import admin

from .models import (
    Categoria, Marca, Proveedor, Producto, ImagenProducto,
    Cliente, Pedido, DetallePedido, Pago, Envio
)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "activa")
    list_filter = ("activa",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "email", "telefono")
    search_fields = ("nombre", "email")
    ordering = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "id", "nombre", "precio", "stock",
        "categoria", "marca", "activo"
    )
    list_filter = ("categoria", "marca", "activo")
    search_fields = ("nombre", "descripcion", "marca__nombre")
    ordering = ("nombre",)
    list_editable = ("precio", "stock", "activo")


@admin.register(ImagenProducto)
class ImagenProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "producto", "principal", "orden")
    list_filter = ("principal",)
    search_fields = ("producto__nombre",)
    ordering = ("producto", "orden")


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "telefono", "direccion")
    search_fields = ("usuario__username", "usuario__email")
    ordering = ("id",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "fecha", "estado", "total")
    list_filter = ("estado", "fecha")
    search_fields = ("cliente__usuario__username",)
    ordering = ("-fecha",)


@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "pedido", "producto", "cantidad", "precio_unitario")
    search_fields = ("producto__nombre",)
    ordering = ("id",)


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("id", "pedido", "metodo", "estado", "monto")
    list_filter = ("metodo", "estado")
    ordering = ("id",)


@admin.register(Envio)
class EnvioAdmin(admin.ModelAdmin):
    list_display = ("id", "pedido", "direccion", "estado")
    list_filter = ("estado",)
    search_fields = ("direccion", "numero_seguimiento")
    ordering = ("id",)
