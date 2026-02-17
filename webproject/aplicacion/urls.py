# Rutas para mi servidor http://127.0.0.1
from django.urls import path

# Los metodos que tenemos en views.py
from aplicacion import views

# Creamos las rutas
urlpatterns = [
    path("", views.index, name="index"),
    path("prueba/", views.prueba, name="prueba"), 

]