from django.shortcuts import render
from markdown2 import Markdown
from . import util
import random

def convertidor(archivo):
    info = util.get_entry(archivo)
    markdowner = Markdown()

    if info == None:
        return None
    else:
        return markdowner.convert(info)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entrada(request, archivo):
    
    contenido_html = convertidor(archivo)

    if contenido_html == None:
        return render(request, "encyclopedia/error.html")
    
    else:
        return render(request, "encyclopedia/entry.html", {
            "titulo": archivo,
            "contenido": contenido_html,
        })
    
def busqueda(request):
    if request.method == "POST":
        entry_search = request.POST['bus']
        contenido_html = convertidor(entry_search)

        if contenido_html == None:

            entradas = util.list_entries()
            recomendaciones = []

            for entrada in entradas:
                if entry_search.lower() in entrada.lower():
                    recomendaciones.append(entrada)
            
            return render(request, "encyclopedia/busqueda.html", {
                "recomendaciones": recomendaciones,
            })

        else:
            return render(request, "encyclopedia/entry.html", {
                "titulo": entry_search,
                "contenido": contenido_html,
            })

def nueva_pagina(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    
    else:
        titulo = request.POST["titulo"]
        contenido = request.POST["contenido"]

        tituloExiste = util.get_entry(titulo)
        if tituloExiste != None:
            return render(request, "encyclopedia/error.html")
        
        else:
            util.save_entry(titulo, contenido)
            contenido_html = convertidor(titulo)
            return render(request, "encyclopedia/entry.html", {
                "titulo": titulo,
                "contenido": contenido_html,
            })

def editar(request):
    if request.method == "POST":
        titulo = request.POST["titulo_entrada"]
        contenido = util.get_entry(titulo)
        return render(request, "encyclopedia/editar.html", {
                "titulo": titulo,
                "contenido": contenido,
        })
    

def guardar(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        contenido = request.POST["contenido"]
        util.save_entry(titulo, contenido)
        contenido_html = convertidor(titulo)
        return render(request, "encyclopedia/entry.html", {
            "titulo": titulo,
            "contenido": contenido_html,
        })

def randome(request):
    entradas = util.list_entries()
    rand_entrada = random.choice(entradas)
    contenido_html = convertidor(rand_entrada)

    return render(request, "encyclopedia/entry.html", {
        "titulo": rand_entrada,
        "contenido": contenido_html,
    })

