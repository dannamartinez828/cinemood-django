from django.db import models


class Pelicula(models.Model):
    ANIMOS = [
        ("feliz", "Feliz"),
        ("triste", "Triste"),
        ("estresado", "Estresado/a"),
        ("aburrido", "Aburrido/a"),
        ("romantico", "Romántico/a"),
    ]

    titulo = models.CharField(max_length=120)
    sinopsis = models.TextField()
    genero = models.CharField(max_length=60)
    animo = models.CharField(max_length=20, choices=ANIMOS)
    anio = models.PositiveIntegerField()
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    emoji = models.CharField(max_length=5, default="🎬")

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo
