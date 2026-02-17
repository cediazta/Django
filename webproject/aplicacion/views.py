from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Creamos metodos para dibujar las vistas
def index(request):
    return render(request, "aplicacion/index.html")

def prueba(request):
    return render(request, "prueba.html")
