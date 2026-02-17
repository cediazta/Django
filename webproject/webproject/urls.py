from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('aplicacion/', include("aplicacion.urls")),
    path('admin/', admin.site.urls),
]

