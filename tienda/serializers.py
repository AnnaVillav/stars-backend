from rest_framework import serializers

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


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

    def validate(self, attrs):
        precio = attrs.get("precio", getattr(self.instance, "precio", None))
        precio_oferta = attrs.get(
            "precio_oferta",
            getattr(self.instance, "precio_oferta", None)
        )

        if precio_oferta is not None and precio is not None:
            if precio_oferta > precio:
                raise serializers.ValidationError({
                    "precio_oferta": "El precio de oferta no puede superar el precio normal."
                })

        return attrs


class ProductoDetalleSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    marca = MarcaSerializer(read_only=True)
    proveedor = ProveedorSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = "__all__"

class ImagenProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProducto
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"


class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = "__all__"

class PedidoDetalleSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    detalles = DetallePedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = "__all__"

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = "__all__"


class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = "__all__"