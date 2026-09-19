from django.shortcuts import get_object_or_404, render

from .models import Pelicula


def inicio(request):
    peliculas_destacadas = Pelicula.objects.all()[:4]
    context = {
        "peliculas": peliculas_destacadas,
        "total_peliculas": Pelicula.objects.count(),
    }
    return render(request, "peliculas/inicio.html", context)


def catalogo(request):
    animo = request.GET.get("animo", "")
    peliculas = Pelicula.objects.all()
    if animo:
        peliculas = peliculas.filter(animo=animo)
    context = {
        "peliculas": peliculas,
        "animo_actual": animo,
        "animos": Pelicula.ANIMOS,
    }
    return render(request, "peliculas/catalogo.html", context)


def detalle(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    context = {"pelicula": pelicula}
    return render(request, "peliculas/detalle.html", context)


def acerca_de(request):
    return render(request, "peliculas/acerca_de.html")
