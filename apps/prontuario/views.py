from django.shortcuts import render
from apps.prontuario.services.prontuario_service import ProntuarioService


def criar_prontuario(request):
    if request.method == "POST":
        paciente_id = request.POST.get("paciente_id")

        prontuario = ProntuarioService.iniciar_prontuario(paciente_id)

        return render(request, "sucesso.html", {"prontuario": prontuario})