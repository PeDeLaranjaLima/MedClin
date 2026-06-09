from .models import *


def cadastrar_medicamento(dados):

    medicamento = Medicamento.objects.create(
        **dados
    )

    return medicamento


def listar_medicamentos():

    return Medicamento.objects.all()


def verificar_estoque_baixo():

    return Medicamento.objects.filter(
        quantidade_estoque__lte=models.F(
            "quantidade_minima"
        )
    )


def dispensar_medicamento(
    medicamento_id,
    farmaceutico_id,
    prontuario_id,
    quantidade
):


medicamento = Medicamento.objects.get(
    id=medicamento_id
)


if medicamento.quantidade_estoque < quantidade:

    raise ValueError(
        "Estoque insuficiente"
    )


medicamento.quantidade_estoque -= quantidade

medicamento.save()


disp = MedicamentoDispensado.objects.create(
    medicamento=medicamento,
    farmaceutico_id=farmaceutico_id,
    prontuario_id=prontuario_id,
    quantidade=quantidade
)


return disp