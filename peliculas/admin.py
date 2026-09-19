from django.contrib import admin

from .models import Pelicula


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "genero", "animo", "anio")
    list_filter = ("animo", "genero")
    search_fields = ("titulo",)
