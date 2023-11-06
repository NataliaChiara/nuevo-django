from django.shortcuts import render, redirect
from inicio.models import Paleta
from inicio.forms import CrearPaletaFormulario, BusquedaPaletaFormulario

def inicio(request):
    return render(request, 'inicio/inicio.html', {})

def paletas(request):
    # marca_a_buscar = request.GET.get('marca')
    # if marca_a_buscar:
    #     listado_de_paletas = Paleta.objects.filter(marca__icontains = marca_a_buscar)
    # else:
    #     listado_de_paletas = Paleta.objects.all() FORMA HTML

    formulario = BusquedaPaletaFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        listado_de_paletas = Paleta.objects.filter(marca__icontains = marca_a_buscar)

    formulario = BusquedaPaletaFormulario()
    return render(request, 'inicio/paletas.html', {'formulario': formulario, 'listado_de_paletas': listado_de_paletas}) 
    
def crear_paleta(request):
    # if request.method == 'POST':
    #     marca = request.POST.get('marca')
    #     descripcion = request.POST.get('descripcion')
    #     anio = request.POST.get('anio')
    #     paleta = Paleta(marca=marca, descripcion=descripcion, anio = anio)
    #     paleta.save() FORMA HTML

    if request.method == 'POST':
        formulario = CrearPaletaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            paleta = Paleta(marca=marca.lower(), descripcion=descripcion, anio=anio)
            paleta.save() #esto lo guarda en la base de datos cuando se accede a la pagina '/paletas/crear'
            return redirect('paletas')
        else:
            return render(request, 'inicio/crear_paleta.html' , {'formulario': formulario})

    formulario = CrearPaletaFormulario()
    return render(request, 'inicio/crear_paleta.html' , {'formulario': formulario})