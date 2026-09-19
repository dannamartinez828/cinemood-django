from unittest.mock import Mock, patch

import requests
from django.test import TestCase
from django.test import override_settings
from django.urls import reverse


class RecomendacionesTests(TestCase):
    @override_settings(MICROSERVICIO_URL="https://cinemood-prueba.onrender.com")
    @patch("recomendaciones.views.requests.get")
    def test_resultado_muestra_datos_del_microservicio(self, get_mock):
        respuesta_api = Mock()
        respuesta_api.raise_for_status.return_value = None
        respuesta_api.json.return_value = {
            "recomendaciones": [
                {
                    "titulo": "Película remota",
                    "genero": "Comedia",
                    "anio": 2025,
                    "compatibilidad": 95,
                    "razon": "Combina con tu ánimo",
                }
            ]
        }
        get_mock.return_value = respuesta_api

        respuesta = self.client.get(
            reverse("recomendaciones:resultado", args=["feliz"])
        )
        self.assertContains(respuesta, "Película remota")

    @override_settings(MICROSERVICIO_URL="https://cinemood-prueba.onrender.com")
    @patch("recomendaciones.views.requests.get")
    def test_no_hay_recomendacion_local_si_falla_servicio(self, get_mock):
        get_mock.side_effect = requests.ConnectionError()
        respuesta = self.client.get(
            reverse("recomendaciones:resultado", args=["feliz"])
        )
        self.assertContains(respuesta, "depende de él")
        self.assertNotContains(respuesta, "% compatible")

    @override_settings(MICROSERVICIO_URL="")
    @patch("recomendaciones.views.requests.get")
    def test_sin_url_no_intenta_usar_un_servicio_local(self, get_mock):
        respuesta = self.client.get(
            reverse("recomendaciones:resultado", args=["feliz"])
        )
        self.assertContains(respuesta, "no utiliza un microservicio local")
        get_mock.assert_not_called()
