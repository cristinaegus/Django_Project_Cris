from django.contrib.auth.models import User
from django.shortcuts import render

def ejemplo_view(request):
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password=password)
            mensaje = 'Usuario registrado correctamente.'
        else:
            mensaje = 'El nombre de usuario ya existe.'
    return render(request, 'ejemplo.html', {'mensaje': mensaje})
