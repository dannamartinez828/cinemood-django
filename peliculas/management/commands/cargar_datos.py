from django.core.management.base import BaseCommand

from peliculas.models import Pelicula


PELICULAS = [
    ("Paddington 2", "Un oso amable demuestra que la bondad cambia una comunidad.", "Comedia", "feliz", 2017, 103, "🐻"),
    ("Sing Street", "Un joven forma una banda para impresionar a una chica.", "Musical", "feliz", 2016, 106, "🎸"),
    ("Intensa-Mente", "Las emociones de Riley aprenden a trabajar juntas.", "Animación", "triste", 2015, 95, "🧠"),
    ("El viaje de Chihiro", "Una niña descubre su valentía en un mundo mágico.", "Fantasía", "triste", 2001, 125, "🐉"),
    ("Mi vecino Totoro", "Dos hermanas encuentran calma y magia en el campo.", "Animación", "estresado", 1988, 86, "🌱"),
    ("Chef", "Un chef recupera la alegría cocinando en un camión.", "Comedia", "estresado", 2014, 114, "🌮"),
    ("Spider-Man: Un nuevo universo", "Miles descubre que cualquiera puede llevar la máscara.", "Aventura", "aburrido", 2018, 117, "🕷️"),
    ("Knives Out", "Una detective historia de secretos y sospechosos.", "Misterio", "aburrido", 2019, 130, "🔎"),
    ("Cuestión de tiempo", "Un joven usa un don familiar para encontrar el amor.", "Romance", "romantico", 2013, 123, "⏳"),
    ("Amélie", "Una joven parisina decide mejorar en secreto la vida de otros.", "Romance", "romantico", 2001, 122, "💌"),
]


class Command(BaseCommand):
    help = "Carga el catálogo de demostración de CineMood"

    def handle(self, *args, **options):
        for titulo, sinopsis, genero, animo, anio, duracion, emoji in PELICULAS:
            Pelicula.objects.update_or_create(
                titulo=titulo,
                defaults={
                    "sinopsis": sinopsis,
                    "genero": genero,
                    "animo": animo,
                    "anio": anio,
                    "duracion": duracion,
                    "emoji": emoji,
                },
            )
        self.stdout.write(self.style.SUCCESS(f"Catálogo listo: {len(PELICULAS)} películas."))
