from django.urls import path
from television import views

urlpatterns = [
    path("", views.index, name="index"),
]
