from django.shortcuts import render
from django.http import HttpResponse
from AppCorder.models import Profesor # puedo usar esta opcion para importar solo Profesor
from AppCorder.models import * #puedo usar esta opcion para importart todo

# Create your views here.

def inicio(request):
    return HttpResponse("Hola, Bienvenido a mi pagina.")


def agregar_profesor(request):

    profe1 = Profesor(nombre = "pepe", apellido = "perez", email = "pepe@python.com", profesion = "profesor")
    profe1.save()

    return HttpResponse(f"Hemos Agregado al profesor {profe1.nombre} a la base de datos")

