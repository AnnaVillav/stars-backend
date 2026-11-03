from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre



class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    precio_oferta = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)]
    )
    stock = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="productos"
    )
    marca = models.ForeignKey(
        Marca,
        on_delete=models.PROTECT,
        related_name="productos"
    )
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT,
        related_name="productos"
    )

    def __str__(self):
        return self.nombre


class ImagenProducto(models.Model):
    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        related_name="imagenes"
    )
    imagen = models.ImageField(upload_to="productos/")
    principal = models.BooleanField(default=False)
    orden = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"


class Cliente(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="cliente"
    )
    telefono = models.CharField(max_length=30, blank=True)
    direccion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.usuario.username


class Pedido(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("confirmado", "Confirmado"),
        ("cancelado", "Cancelado"),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name="pedidos"
    )
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="pendiente"
    )
    total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"Pedido #{self.id}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="detalles"
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name="detalles_pedido"
    )
    cantidad = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    precio_unitario = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"


class Pago(models.Model):
    METODOS = [
        ("efectivo", "Efectivo"),
        ("transferencia", "Transferencia"),
        ("tarjeta", "Tarjeta simulada"),
    ]

    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("aprobado", "Aprobado"),
        ("rechazado", "Rechazado"),
    ]

    pedido = models.OneToOneField(
        Pedido,
        on_delete=models.CASCADE,
        related_name="pago"
    )
    metodo = models.CharField(max_length=20, choices=METODOS)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="pendiente"
    )
    monto = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return f"Pago del pedido #{self.pedido_id}"


class Envio(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("preparando", "Preparando"),
        ("enviado", "Enviado"),
        ("entregado", "Entregado"),
    ]

    pedido = models.OneToOneField(
        Pedido,
        on_delete=models.CASCADE,
        related_name="envio"
    )
    direccion = models.CharField(max_length=255)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="pendiente"
    )
    numero_seguimiento = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f"Envío del pedido #{self.pedido_id}"
