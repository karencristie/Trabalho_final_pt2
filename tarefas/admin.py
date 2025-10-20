# tarefas/admin.py

from django.contrib import admin
from .models import Demanda

# Crie uma classe para customizar a exibição no admin
class DemandaAdmin(admin.ModelAdmin):
    # Define as colunas que você quer ver na lista
    list_display = ('titulo', 'responsavel', 'grau_urgencia', 'solicitante', 'data_criacao')
    
    # Adiciona um filtro na lateral direita
    list_filter = ('grau_urgencia', 'responsavel')
    
    # Adiciona um campo de busca
    search_fields = ('titulo', 'descricao')

# Registra o modelo Demanda usando a classe de customização
admin.site.register(Demanda, DemandaAdmin)