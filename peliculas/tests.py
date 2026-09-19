from django.test import TestCase
from django.urls import reverse

from .models import Pelicula


class PeliculasTests(TestCase):
    def setUp(self):
        self.pelicula = Pelicula.objects.create(
            titulo="Prueba",
            sinopsis="Una película de prueba",
            genero="Comedia",
            animo="feliz",
            anio=2024,
            duracion=90,
        )

    def test_catalogo_consulta_modelo(self):
        respuesta = self.client.get(reverse("peliculas:catalogo"))
        self.assertContains(respuesta, "Prueba")

    def test_detalle_usa_parametro_dinamico(self):
        respuesta = self.client.get(
            reverse("peliculas:detalle", args=[self.pelicula.id])
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Una película de prueba")

    def test_detalle_inexistente_responde_404(self):
        respuesta = self.client.get(reverse("peliculas:detalle", args=[999]))
        self.assertEqual(respuesta.status_code, 404)
