from django.db import models


class Farmaceutico(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    crf = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Medicamento(models.Model):
    nome = models.CharField(max_length=100)

    numero_lote = models.CharField(max_length=50)

    quantidade_estoque = models.IntegerField()

    quantidade_minima = models.IntegerField()

    data_validade = models.DateField()

    def __str__(self):
        return self.nome


class MedicamentoDispensado(models.Model):

    medicamento = models.ForeignKey(
        Medicamento,
        on_delete=models.CASCADE
    )

    farmaceutico = models.ForeignKey(
        Farmaceutico,
        on_delete=models.CASCADE
    )

    prontuario_id = models.IntegerField()

    quantidade = models.IntegerField()

    data_dispensacao = models.DateTimeField(
        auto_now_add=True
    )


class EstoqueMedicamento(models.Model):

    gestor_id = models.IntegerField()

    medicamento = models.ForeignKey(
        Medicamento,
        on_delete=models.CASCADE
    )


class GestorMedicamento(models.Model):

    gestor_id = models.IntegerField()

    medicamento = models.ForeignKey(
        Medicamento,
        on_delete=models.CASCADE
    )