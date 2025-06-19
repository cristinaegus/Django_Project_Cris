from django.db import models

class Producto(models.Model):
    codigo_inventario = models.CharField(max_length=100)
    tipo_producto = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo_inventario} - {self.marca}"
