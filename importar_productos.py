import csv
from MiWeb.models import Producto
from django.db import connection

with open('productos.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Evita duplicados por codigo_inventario
        if not Producto.objects.filter(codigo_inventario=row['codigo_inventario']).exists():
            producto = Producto.objects.create(
                codigo_inventario=row['codigo_inventario'],
                tipo_producto=row['tipo_producto'],
                marca=row['marca'],
                precio_producto=row['precio_producto'],
                fecha_venta=row['fecha_venta'] or None,
                disponible=bool(int(row['disponible']))
            )
            # Si el CSV tiene id_producto y quieres que coincida, actualiza el id manualmente
            if 'id_producto' in row and row['id_producto']:
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE MiWeb_producto SET id = %s WHERE id = %s",
                        [row['id_producto'], producto.id]
                    )

