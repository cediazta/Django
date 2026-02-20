from django.urls import path
from formularios import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ejemplo/", views.ejemplo, name="ejemplo"),
    path("saludo/", views.saludo, name="saludo"),
    path("sumarnumeros/", views.sumar, name="sumarnumeros"),
    path("parimpar/", views.parimpar, name="parimpar"),
    path("collatz/", views.collatz, name="collatz"),
    path("tabla/", views.multiplcar, name="tabla"),
    path("tablav2/", views.multiplcarv2, name="tablav2"),
    path("deportes/", views.deportes, name="deportes"),
    path("colores/", views.colores, name="colores"),
    path("coloresv2/", views.colores, name="coloresv2"),
    path("comics/", views.comics, name="comics"),
    
]