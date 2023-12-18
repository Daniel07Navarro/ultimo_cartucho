from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pais
from django.contrib import messages

def Pais1(request):
    paisListado = Pais.objects.all()
    return render(request, 'Paises.html', {"pai": paisListado})

def RegistrarPais(request):
    return render(request, 'RegistrarPais.html', {})

def Editoriales(request):
    return render(request, 'Editoriales.html', {})

def CrearEditorial(request):
    return render(request, 'CrearEditorial.html', {})


def index(request):
    return render(request, 'index.html')  # Reemplaza 'index.html' con el nombre de tu plantilla
# mi_aplicacion/views.py

def eliminar_pais(request,idpais):
    pais=Pais.objects.get(idpais=idpais)
    pais.delete()
    return redirect('/Paises/')

def registrar_pais(request):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']
    poblacion=request.POST['poblacion']
    estado=request.POST['estado']
    pais=Pais.objects.create(codigo=codigo,nombre=nombre,poblacion=poblacion,estado=estado)
    messages.success(request, f'Se agregó correctamente el artículo {pais.nombre}')
    return redirect('/Paises/')