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
    
def multiplcar(request):
    if "cajanumero" in request.POST:
        listanumeros = []
        contador = 1
        num = 0
        numero = int(request.POST["cajanumero"])
        while contador <= 10:
            num = numero * contador
            listanumeros.append(num)
            contador +=1
        informacion = {
            "listanumeros": listanumeros
        }
        return render(request, "paginas/tabla.html", informacion)       
    else:
        return render(request, "paginas/tabla.html")

def multiplcarv2(request):
    if "cajanumero" in request.POST:
        listadatos = []
        numero = int(request.POST["cajanumero"])
        for i in range(1,11):
            operacion = f"{numero} * {i}"
            resultado = numero * i
            listadatos.append(
                {
                    "operacion": operacion,
                    "resultado": resultado
                }
            )
        informacion = {
            "listadatos": listadatos
        }
        return render(request, "paginas/tablav2.html", informacion)       
    else:
        return render(request, "paginas/tablav2.html")

def deportes(request):
    listaDeportes = ["Futbol", "Petanca", "Curling", "Dardos", "Parhis", "Rana",]
    if "selectdeporte" in request.POST:
        deporte = request.POST["selectdeporte"]
        informacion = {
            "listadeportes": listaDeportes,
            "deporte": deporte
        }
        return render(request, "paginas/deportes.html", informacion)
    else:
        informacion = {
            "listadeportes": listaDeportes
        }
        return render(request, "paginas/deportes.html", informacion)

def colores(request):
    listaColores = ["Azul", "Rojo", "Verde", "Amarillo", "Morado",]
    if "selectcolor" in request.POST:
        color = request.POST["selectcolor"]
        informacion = {
            "listacolores": listaColores,
            "selectcolor": color
        }
        return render(request, "paginas/colores.html", informacion)
    else:
        informacion = {
            "listacolores": listaColores
        }
        return render(request, "paginas/colores.html", informacion)

def colores(request):
    listaColores = [
        {
            "nombrecolor": "Rojo",
            "valor": "red"
        },
        {
            "nombrecolor": "Amarillo",
            "valor": "yellow"
        },
        {
            "nombrecolor": "Verde",
            "valor": "lightgreen"
        },
        {
            "nombrecolor": "Azul",
            "valor": "lightblue"
        }
    ]
    if ('selectcolores' in request.POST):
        colorSeleccionado = request.POST["selectcolores"]
        informacion = {
            "listacolores": listaColores,
            "color": colorSeleccionado
        }
        return render(request, "paginas/coloresv2.html", informacion)
    else:
        informacion = {
            "listacolores": listaColores
        }
        return render(request, "paginas/coloresv2.html", informacion)

def comics(request):
    listacomics = [
        {
            "index": 0,
            "titulo": "Spiderman",
            "imagen": "https://elcoleccionistacomics.com/60266-medium_default/spiderman-de-todd-mcfarlane-vol1-de-6.jpg"
        },
        {
            "index": 1,
            "titulo": "Spawn",
            "imagen": "https://m.media-amazon.com/images/I/91hZO1pjAoL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "index": 2,
            "titulo": "Wolverine",
            "imagen": "https://www.kamekame.es/53918-large_default/marvel-omnibus-dinastia-de-x-potencias-de-x-comic.jpg"
        },
        {
            "index": 3,
            "titulo": "Wolverine",
            "imagen": "https://www.kamekame.es/53918-large_default/marvel-omnibus-dinastia-de-x-potencias-de-x-comic.jpg"
        },
        {
            "index": 4,
            "titulo": "Asterix y Obelix",
            "imagen": "https://comicsbarcelona.com/wp-content/uploads/2015/11/127913-Asterix-2.-La-Hoz-de-Oro.jpg"
        } 
               
              
    ]
    
    if "selectcomic" in request.POST:
        indice = int(request.POST["selectcomic"])
        comic = listacomics[indice]
        informacion = {
            "listacomics": listacomics,
            "comic": comic,

        }
        return render(request, "paginas/comics.html", informacion)
    else:
        return render(request, "paginas/comics.html")
