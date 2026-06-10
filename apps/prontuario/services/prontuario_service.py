from apps.prontuario.models import Prontuario, Observacao, Prescricao


class ProntuarioService:

    @staticmethod
    def iniciar_prontuario(paciente):
        return Prontuario.objects.create(paciente=paciente)

    @staticmethod
    def adicionar_observacao(prontuario, texto):
        return Observacao.objects.create(
            prontuario=prontuario,
            texto=texto
        )

    @staticmethod
    def gerar_prescricao(prontuario, descricao):
        # desativa anteriores
        Prescricao.objects.filter(prontuario=prontuario, ativa=True).update(ativa=False)

        return Prescricao.objects.create(
            prontuario=prontuario,
            descricao=descricao,
            ativa=True
        )

    @staticmethod
    def obter_prescricao_ativa(prontuario):
        return Prescricao.objects.filter(
            prontuario=prontuario,
            ativa=True
        ).first()