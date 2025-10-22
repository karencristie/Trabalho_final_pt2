# tarefas/admin.py

from django.contrib import admin
from .models import Demanda, Profissional # <-- 1. Importe o Profissional

# --- 2. REGISTRE O NOVO MODELO ---
@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome',)
# ----------------------------------

# Crie uma classe para customizar a exibição no admin
@admin.register(Demanda) # <-- Isso é o mesmo que admin.site.register(Demanda, DemandaAdmin)
class DemandaAdmin(admin.ModelAdmin):
    # ... (todo o resto do seu DemandaAdmin)
    list_display = ('titulo', 'status', 'responsavel', 'grau_urgencia', 'solicitante', 'data_criacao', 'descricao_curta')
    list_filter = ('status', 'grau_urgencia', 'responsavel')
    search_fields = ('titulo', 'descricao')
    # ... (sua função descricao_curta)
    def descricao_curta(self, obj):
        # ...
        return obj.descricao

# Crie uma classe para customizar a exibição no admin
class DemandaAdmin(admin.ModelAdmin):
    # Define as colunas que você quer ver na lista
    # Adicionamos 'descricao_curta'
    list_display = ('titulo', 'responsavel', 'grau_urgencia', 'solicitante', 'data_criacao', 'descricao_curta')
    
    # Adiciona um filtro na lateral direita
    list_filter = ('status','grau_urgencia', 'responsavel')
    
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

