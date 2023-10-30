from django.shortcuts import render
from inicio.models import Paleta

def inicio(request):
    return render(request, 'inicio/inicio.html', {})

def paletas(request):
    paleta = Paleta(marca='Wilson', descripcion='paleta de bela', anio = 2022)
    paleta.save() #esto lo guarda en la base de datos cuando se accede a la pagina '/paletas'
    return render(request, 'inicio/paletas.html', {'paleta': paleta})