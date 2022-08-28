from tokenize import group
from django.contrib import admin
from .models import Mercadoria
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header = 'Estoque'

class adminMercadoria(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'descricao', 'quantidadeInicial', 'unidadeMedida')

admin.site.register(Mercadoria, adminMercadoria)
admin.site.unregister(Group)