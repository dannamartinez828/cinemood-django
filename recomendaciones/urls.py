from django.urls import path

from . import views

app_name = "recomendaciones"

urlpatterns = [
    path("", views.elegir_animo, name="elegir"),
    path("animo/<str:animo>/", views.resultado, name="resultado"),
    path("historial/", views.historial, name="historial"),
]
