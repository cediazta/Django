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
    if "cajaid" in request.POST:
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
    elif "dato" in request.GET:
        service = md.ServiceDepartamentos()
        id = int(request.GET["dato"])
        # Buscamos el departamento
        dept = service.buscarDepartamento(id)
        informacion = {
            "departamento": dept,
        }
        return render(request, "actualizardepartamento.html", informacion)
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
    
def delete(request):
    if "dato" in request.GET:
        service = md.ServiceDepartamentos()
        id = int(request.GET["dato"])
        service.deleteDepartamento(id)
        departamentos = service.getDepartamentos()
        informacion = {
            "departamentos": departamentos
        }
        return render(request, "departamentos.html", informacion)
    
def empleadosDepartamento(request):
    service = md.ServiceDepartamentos()
    departamentos = service.getDepartamentos()
    if "cajaiddept" in request.POST:
        iddept = int(request.POST["cajaiddept"])
        empleados = service.buscarEmpleadosDepartamento(iddept)
        informacion = {
            "empleados": empleados,
            "departamentos": departamentos,
        }
        return render(request, "empdept.html", informacion) 
    else:
        informacion = {
            "departamentos": departamentos
        }
        return render(request, "empdept.html", informacion)

def empleadosSalario(request):
    if "cajasalario" in request.POST:
        service = md.ServiceDepartamentos()
        numSalario = int(request.POST["cajasalario"])
        salario = service.buscarEmpleadosSalario(numSalario)
        informacion = {
            "salario": salario,
        }
        return render(request, "empleadossalario.html", informacion)
    else:
        return render(request, "empleadossalario.html")

    