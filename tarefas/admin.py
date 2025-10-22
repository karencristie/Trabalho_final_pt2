# tarefas/admin.py

from django.contrib import admin
from .models import Demanda

# Crie uma classe para customizar a exibição no admin
class DemandaAdmin(admin.ModelAdmin):
    # Define as colunas que você quer ver na lista
    # Adicionamos 'descricao_curta'
    list_display = ('titulo', 'responsavel', 'grau_urgencia', 'solicitante', 'data_criacao', 'descricao_curta')
    
    # Adiciona um filtro na lateral direita
    list_filter = ('grau_urgencia', 'responsavel')
    
    # Adiciona um campo de busca
    search_fields = ('titulo', 'descricao')

    # Nova função para mostrar apenas parte da descrição
    def descricao_curta(self, obj):
        # Retorna os primeiros 50 caracteres da descrição
        if len(obj.descricao) > 50:
            return f"{obj.descricao[:50]}..."
        return obj.descricao
    
    # Define um nome amigável para a coluna no admin
    descricao_curta.short_description = 'Descrição (Trecho)'

# Registra o modelo Demanda usando a classe de customização
admin.site.register(Demanda, DemandaAdmin)