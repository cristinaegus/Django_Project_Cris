from django.contrib.auth.models import User
from django.shortcuts import render
from django.db import connection
from .models import Producto

def ejemplo_view(request):
    mensaje = ''
    if request.method == 'POST':
        # Registro de usuario
        if 'username' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, email=email, password=password)
                mensaje = 'Usuario registrado correctamente.'
            else:
                mensaje = 'El nombre de usuario ya existe.'
        # Registro de producto
        elif 'codigo_inventario' in request.POST:
            codigo_inventario = request.POST.get('codigo_inventario')
            tipo_producto = request.POST.get('tipo_producto')
            marca = request.POST.get('marca')
            precio_producto = request.POST.get('precio_producto')
            fecha_venta = request.POST.get('fecha_venta') or None
            disponible = bool(int(request.POST.get('disponible', 1)))
            Producto.objects.create(
                codigo_inventario=codigo_inventario,
                tipo_producto=tipo_producto,
                marca=marca,
                precio_producto=precio_producto,
                fecha_venta=fecha_venta,
                disponible=disponible
            )
            mensaje = 'Producto agregado correctamente.'
    # Consulta directa a la tabla MiWeb_producto
    with connection.cursor() as cursor:
        cursor.execute('SELECT id, codigo_inventario, tipo_producto, marca, precio_producto, fecha_venta, disponible FROM MiWeb_producto')
        productos = [
            {
                'id': row[0],
                'codigo_inventario': row[1],
                'tipo_producto': row[2],
                'marca': row[3],
                'precio_producto': row[4],
                'fecha_venta': row[5],
                'disponible': row[6],
            }
            for row in cursor.fetchall()
        ]
    return render(request, 'ejemplo.html', {'mensaje': mensaje, 'productos': productos})
