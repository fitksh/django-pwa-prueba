from django.shortcuts import render
from .models import Musician, Album
from django.http import HttpResponse

def crear_musician_get(request, nombre, apellido, instrument='triangulo'):
    musician = Musician(first_name=nombre, last_name=apellido, instrument=instrument)
    musician.save()
    mensaje = f'Musician {nombre} {apellido} creado exitosamente.'
    
    return HttpResponse({mensaje: mensaje})