from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from .services import *


def estoque(request):

    medicamentos = listar_medicamentos()

    return render(
        request,
        "farmacia/estoque.html",
        {
            "medicamentos": medicamentos
        }
    )


def cadastrar_medicamento_view(request):


form = MedicamentoForm()


if request.method == "POST":

    form = MedicamentoForm(
        request.POST
    )

    if form.is_valid():

        cadastrar_medicamento(
            form.cleaned_data
        )

        return redirect(
            "estoque"
        )


return render(
    request,
    "farmacia/cadastrar_medicamento.html",
    {
        "form": form
    }
)


def dispensar_view(
    request,
    medicamento_id
):


medicamento = Medicamento.objects.get(
    id=medicamento_id
)


if request.method == "POST":


dispensar_medicamento(
    medicamento.id,
    1,
    form.cleaned_data["prontuario_id"],
    form.cleaned_data["quantidade"]
)


return redirect(
    "estoque"
)


def editar_medicamento_view(request, medicamento_id):


def historico_dispensacoes_view(request):