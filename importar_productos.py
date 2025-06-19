import csv
from MiWeb.models import Producto

count = 0
with open('productos.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Producto.objects.create(
            codigo_inventario=row['codigo_inventario'],
            tipo_producto=row['tipo_producto'],
            marca=row['marca'],
            precio_producto=row['precio_producto'],
            fecha_venta=row['fecha_venta'] or None,
            disponible=bool(int(row['disponible']))
        )
        count += 1
print(f"¡Importación completada! Productos importados: {count}")
