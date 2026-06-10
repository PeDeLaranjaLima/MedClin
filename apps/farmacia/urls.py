from django.urls import path

from .views import *


urlpatterns = [
    path(
        "",
        estoque,
        name="estoque"
    ),

    path(
        "cadastrar/",
        cadastrar_medicamento_view,
        name="cadastrar_medicamento"
    ),

    path(
        "dispensar/<int:medicamento_id>/",
        dispensar_view,
        name="dispensar"
    ),

    path(
        "editar/<int:medicamento_id>/",
        editar_medicamento_view,
        name="editar_medicamento"
    ),

    path(
        "historico/",
        historico_dispensacoes_view,
        name="historico_dispensacoes"
    ),
]