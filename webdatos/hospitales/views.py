from django.shortcuts import render
# Agregamos la libreria de models.py
from hospitales import models as md

# Create your views here.
def index(request):
    return render(request, "index.html")

def tabladepartamentos(request):
    # Creamos un servicio de departamentos
    service = md.ServiceDepartamentos()
    informacion = {
        "departamentos": service.getDepartamentos(),
    }
    return render(request, "departamentos.html", informacion)

def insertarDepartamento(request):
    if "cajaid" in request.POST:
        service = md.ServiceDepartamentos()
        id = int(request.POST["cajaid"])
        nom = request.POST["cajanombre"]
        loc = request.POST["cajalocalidad"]
        service.insertarDepartamento(id, nom, loc)
        service = md.ServiceDepartamentos()
        informacion = {
            "departamentos": service.getDepartamentos(),
        }
        return render(request, "departamentos.html", informacion)
    else:
        return render(request, "insertardepartamento.html")

def actualizarDepartamento(request):
    if "cajanum" in request.POST:
        service = md.ServiceDepartamentos()
        id = int(request.POST["cajaid"])
        nom = request.POST["cajanombre"]
        loc = request.POST["cajalocalidad"]
        service.actualizarDepartamento(id, nom, loc,)
        service = md.ServiceDepartamentos()
        informacion = {
            "departamentos": service.getDepartamentos(),
        }
        return render(request, "departamentos.html", informacion)
    else:
        return render(request, "actualizardepartamento.html")
    
def buscarDepartamentoForm(request):
    if "cajaid" in request.POST:
        service = md.ServiceDepartamentos()
        id = int(request.POST["cajaid"])
        dept = service.buscarDepartamento(id)
        informacion = {
            "departamento": dept,
        }
        return render(request, "buscarform.html", informacion)
    else:
        return render(request, "buscarform.html")

def buscarDepartamentoGet(request):
    if "dato" in request.GET:
        service = md.ServiceDepartamentos()
        id = int(request.GET["dato"])
        dept = service.buscarDepartamento(id)
        informacion = {
            "departamento": dept,
        }
        return render(request, "buscarget.html", informacion)
    else:
        return render(request, "buscarget.html")
    