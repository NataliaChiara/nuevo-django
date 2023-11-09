from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from cuentas.forms import MiFormularioDeCreacion

def login(request):
    formulario = AuthenticationForm()

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            django_login(request, user)
            return redirect('inicio')
        
    return render(request, 'cuentas/login.html', {'formulario': formulario})

def registro(request):
    formulario = MiFormularioDeCreacion()

    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')

    return render (request, 'cuentas/registro.html', {'formulario': formulario})