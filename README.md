# CineMood Django

Aplicación web que recomienda películas según el estado de ánimo. Este
repositorio contiene únicamente el proyecto Django. Las recomendaciones se
consultan desde un microservicio separado desplegado en Render.

## Preparar el proyecto en Windows

Abre CMD dentro de esta carpeta:

```cmd
py -m venv entorno_virtual
entorno_virtual\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_datos
```

## Conectar con el microservicio de Render

Reemplaza la dirección por tu URL pública:

```cmd
set MICROSERVICIO_URL=https://TU-SERVICIO.onrender.com
python manage.py runserver
```

Abre <http://127.0.0.1:8000>.

## Contenido académico

- Apps `peliculas` y `recomendaciones`.
- Múltiples vistas y templates.
- Modelos `Pelicula` y `PerfilCinefilo`.
- Uso de `render()`, `context` y `get_object_or_404()`.
- Rutas dinámicas con identificador de película y estado de ánimo.
- Una vista consume el microservicio externo con `requests`.

## Pruebas

```cmd
python manage.py test
```
