from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "paginas/index.html")

def ejemplo(request):
    return render(request, "paginas/ejemplo.html")

def saludo(request):
    # Siempre que tengamos un POST debemos preguntar
    if "cajanombre" in request.POST:    
        dato = request.POST["cajanombre"] # coje dato de la caja nombre de saludo.html
        # Enviamos informacion
        informacion = {
            "nombre": dato
        }
        return render(request, "paginas/saludo.html", informacion)
    else:
        # No enviamos informacion
        return render(request, "paginas/saludo.html")
    
def sumar(request):
    if "cajanum1" in request.POST:
        num1 = request.POST["cajanum1"]
        num2 = request.POST["cajanum2"]
        suma = int(num1) + int(num2)
        informacion = {
            "suma": suma
        } 
        return render(request, "paginas/sumarnumeros.html", informacion)
    else:
        return render(request, "paginas/sumarnumeros.html")
    
def parimpar(request):
    if "cajanum" in request.POST:
        num = int(request.POST["cajanum"])
        if num % 2 == 0:
            dato = "Par"
            informacion = {
                "resultado": dato
            }
            return render(request, "paginas/parimpar.html", informacion)
        else:
            dato = "Impar"
            informacion = {
                "resultado": dato
            }
            return render(request, "paginas/parimpar.html", informacion)
    else:
        return render(request, "paginas/parimpar.html")
        
def collatz(request):
    if "cajanumero" in request.POST:
        # TENEMOS DATOS
        # Devolvemos una lista de numeros
        listanumeros = []
        numero = int(request.POST["cajanumero"])
        while numero != 1:
            if numero % 2 == 0:
                numero = numero /2
            else:
                numero = numero * 3 + 1
            listanumeros.append(numero)
        informacion = {
            "listanumeros": listanumeros
        }
    
       # Devolvemos la informacion
        return render(request, "paginas/collatz.html", informacion) 
    else:
        # SIN DATOS
        return render(request, "paginas/collatz.html")
