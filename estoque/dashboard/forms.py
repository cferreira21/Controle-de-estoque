from socket import fromshare
from django import forms
from .models import Mercadoria

class formMercadoria(forms.ModelForm):
    class Meta:
        model = Mercadoria
        fields = ['codigo', 'nome', 'descricao', 'quantidadeInicial', 'unidadeMedida']
