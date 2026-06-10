from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=255)


class Medico(models.Model):
    nome = models.CharField(max_length=255)


class Prontuario(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    data_criacao = models.DateField(auto_now_add=True)
    diagnostico = models.TextField()


class Observacao(models.Model):
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


class Prescricao(models.Model):
    prontuario = models.ForeignKey(Prontuario, on_delete=models.CASCADE)
    descricao = models.TextField()
    ativa = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)