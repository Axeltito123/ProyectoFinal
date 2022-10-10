from django.contrib import admin
from django.urls import path, include
from blog.views import (
    mostrar_inicio,
    procesar_formulario,
    procesar_formulario_2,
    busqueda,
    buscar,
)

urlpatterns = [
    path("inicio/", mostrar_inicio),
    path("formulario/", procesar_formulario, name="formulario"),
    path("formulario-2", procesar_formulario_2, name="formulario_2"),
    path("busqueda/", busqueda, name="busqueda"),
    path("buscar/", buscar),
]
