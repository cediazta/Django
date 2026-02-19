from django.urls import path
from formularios import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ejemplo/", views.ejemplo, name="ejemplo"),
    path("saludo/", views.saludo, name="saludo"),
    path("sumarnumeros/", views.sumar, name="sumarnumeros"),
    path("parimpar/", views.parimpar, name="parimpar"),
    path("collatz/", views.collatz, name="collatz"),
          
]