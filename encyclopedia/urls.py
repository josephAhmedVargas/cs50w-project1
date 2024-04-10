from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:archivo>", views.entrada, name="entrada"),
    path("search", views.busqueda, name="busqueda"),
    path("new", views.nueva_pagina, name="nueva_pagina"),
    path("edit", views.editar, name="editar"),
    path("save_edit", views.guardar, name="guardar"),
    path("rand", views.randome, name="randome"),  
]
