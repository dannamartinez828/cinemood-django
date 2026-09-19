from django.urls import path

from . import views

app_name = "peliculas"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("peliculas/", views.catalogo, name="catalogo"),
    path("peliculas/<int:pelicula_id>/", views.detalle, name="detalle"),
    path("acerca-de/", views.acerca_de, name="acerca_de"),
]
