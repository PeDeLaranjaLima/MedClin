from django import forms

from .models import Medicamento


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = [
            "nome",
            "numero_lote",
            "quantidade_estoque",
            "quantidade_minima",
            "data_validade",
        ]


class DispensacaoForm(forms.Form):
    prontuario_id = forms.IntegerField()

    quantidade = forms.IntegerField(
        min_value=1
    )