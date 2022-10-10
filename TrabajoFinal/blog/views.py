from sqlite3 import Cursor
from django.http import HttpResponse
from django.shortcuts import render
from blog.forms import AutorFormulario
from blog.models import Autor

# Create your views here.


def mostrar_inicio(request):
    return render(request, "blog/inicio.html")


def procesar_formulario(request):
    if request.method != "POST":
        return render(request, "blog/formulario.html")

    autor = Autor(nombre=request.POST["autor"], profesion=request.POST["profesion"])
    autor.save()
    return render(request, "blog/inicio.html")


def procesar_formulario_2(request):
    if request.method != "POST":
        mi_formulario = AutorFormulario()
    else:
        mi_formulario = AutorFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            autor = Autor(
                nombre=informacion["autor"], profesion=informacion["profesion"]
            )
            autor.save()
            return render(request, "blog/inicio.html")

    contexto = {"formulario": mi_formulario}

    return render(request, "blog/formulario_2.html", contexto)


def busqueda(request):
    return render(request, "blog/busqueda.html")


def buscar(request):
    respuesta = f"Buscando la camada nro: {request.GET['camada']}"
    return HttpResponse(respuesta)  # TODO: podríamos mostrarla, no?
