import requests
from django.conf import settings
from django.shortcuts import redirect, render

from peliculas.models import Pelicula
from .models import PerfilCinefilo


def elegir_animo(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "Cinéfilo").strip() or "Cinéfilo"
        animo = request.POST.get("animo", "")
        animos_validos = {valor for valor, _ in Pelicula.ANIMOS}
        if animo in animos_validos:
            PerfilCinefilo.objects.create(nombre=nombre, animo_favorito=animo)
            request.session["nombre"] = nombre
            return redirect("recomendaciones:resultado", animo=animo)

    context = {"animos": Pelicula.ANIMOS}
    return render(request, "recomendaciones/elegir.html", context)


def resultado(request, animo):
    """Consume el microservicio; no calcula recomendaciones localmente."""
    nombre = request.session.get("nombre", "Cinéfilo")
    microservicio_url = settings.MICROSERVICIO_URL

    if not microservicio_url:
        recomendaciones = []
        peliculas_locales = []
        error = (
            "Falta configurar la URL pública de Render en MICROSERVICIO_URL. "
            "CineMood no utiliza un microservicio local."
        )
    else:
        url = f"{microservicio_url}/api/recomendaciones/{animo}"
        try:
            respuesta = requests.get(url, timeout=8)
            respuesta.raise_for_status()
            datos = respuesta.json()
            recomendaciones = datos.get("recomendaciones", [])
            error = None
            # El modelo local solo se consulta después de recibir la respuesta remota.
            peliculas_locales = Pelicula.objects.filter(animo=animo)
        except (requests.RequestException, ValueError):
            recomendaciones = []
            peliculas_locales = []
            error = (
                "El microservicio de Render no está disponible. CineMood depende "
                "de él y no genera recomendaciones locales."
            )

    context = {
        "nombre": nombre,
        "animo": animo,
        "recomendaciones": recomendaciones,
        "peliculas_locales": peliculas_locales,
        "error": error,
        "microservicio_url": microservicio_url or "Sin configurar",
    }
    return render(request, "recomendaciones/resultado.html", context)


def historial(request):
    perfiles = PerfilCinefilo.objects.order_by("-fecha_creacion")[:10]
    context = {"perfiles": perfiles}
    return render(request, "recomendaciones/historial.html", context)
