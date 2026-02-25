from django.shortcuts import render
from television import models as md

# Create your views here.
def index(request):
    return render(request, "index.html")

def series(request):
    service = md.ServiceSeries()
    listaSeries = service.getSeries()
    informacion = {
        "listaseries": listaSeries
    }
    return render(request, "series.html", informacion)

def personaje(request):
    if "idserie" in request.GET:
        service = md.ServiceSeries()
        idserie = int(request.GET["idserie"])
        personajes = service.getPersonajesSerie(idserie)
        informacion = {
            "personajes": personajes,
        }
        return render(request, "personajes.html", informacion)
    else:
        return render(request, "personajes.html")
    
def insertar(request):
    service = md.ServiceSeries()
    listaSeries = service.getSeries()
    informacion = {
        "listaseries": listaSeries
    }
    if "cajanombre" in request.POST:
        nombre = request.POST["cajanombre"]
        imagen = request.POST["cajaimagen"]
        idserie = request.POST["cajaidserie"]
        service.insertarPersonaje(nombre, imagen, idserie)
        return render(request, "insertar.html", informacion)
    else:
        return render(request, "insertar.html", informacion)
        
