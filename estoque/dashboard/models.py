from django.db import models

# Create your models here.
class Mercadoria(models.Model):
    nome = models.CharField(max_length=20, null=True)
    descricao = models.CharField(max_length=20, null=True)
    codigo = models.PositiveIntegerField(null=True)
    quantidadeInicial = models.PositiveIntegerField(null=True)
    unidadeMedida = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.codigo} - {self.nome} ({self.quantidadeInicial}) ({self.unidadeMedida})'
