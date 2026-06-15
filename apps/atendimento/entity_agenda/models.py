# Representa a Entity Agenda, controlando a agenda da clínica e o registro das consultas.
#
# Atributos conforme o Mapeamento Objeto-Relacional (tabela Agenda):
# idAgenda, data, horariosProfissionais, ocupacaoSalas
#
# A tabela Recepcionista_Agenda representa a associação entre recepcionistas e agendas

from django.db import models


class Agenda(models.Model):
    idAgenda = models.AutoField(
        primary_key=True,
        db_column='idAgenda'
    )

    data = models.DateField()

    horariosProfissionais = models.JSONField(
        default=dict
    )

    ocupacaoSalas = models.JSONField(
        default=dict
    )

    class Meta:
        db_table = 'Agenda'
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'

    def __str__(self):
        return f'Agenda {self.idAgenda}'


class Recepcionista_Agenda(models.Model):
    """
    Tabela associativa Recepcionista_Agenda.

    Representa a associação entre recepcionistas e agendas
    """

    """
    idAgenda = models.ForeignKey(
        'atendimento.Agenda',
        on_delete=models.CASCADE,
        db_column='idAgenda',
        related_name='recepcionistas'
    )
    """
    idAgenda = models.IntegerField(
        db_column='idAgenda'
    )

    """
    idRecepcionista = models.ForeignKey(
        'acesso.Recepcionista',
        on_delete=models.CASCADE,
        db_column='idRecepcionista',
        related_name='agendas'
    )
    """
    idRecepcionista = models.IntegerField(
        db_column='idRecepcionista'
    )
    
    class Meta:
        db_table = 'Recepcionista_Agenda'
        verbose_name = 'Acesso de recepcionista a agenda'
        verbose_name_plural = 'Acessos de recepcionistas as agendas'
        unique_together = (('idAgenda', 'idRecepcionista'),)

    def __str__(self):
        return f'Recepcionista {self.idRecepcionista} -> Agenda {self.idAgenda}'
    