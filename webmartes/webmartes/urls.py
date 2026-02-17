from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('practica/', include("practica.urls")),
    path('admin/', admin.site.urls),
]
