from hospitales import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('departamentos/', views.tabladepartamentos, name="departamentos"),
    path('insertdpt/', views.insertarDepartamento, name="insertdpt"),
    path('updatedept/', views.actualizarDepartamento, name="updatedept"),
    path('buscarform/', views.buscarDepartamentoForm, name="buscarform"),
    path('buscarget/', views.buscarDepartamentoGet, name="buscarget"),
    path('delete/', views.delete, name="delete"),
    path('empdept/', views.empleadosDepartamento, name="empdept"),
    path('empsalario/', views.empleadosSalario , name="empsalario"),

]