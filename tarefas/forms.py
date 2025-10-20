# tarefas/forms.py
from django import forms
from .models import Demanda

class DemandaForm(forms.ModelForm):
    class Meta:
        model = Demanda
        # Campos que aparecerão no formulário
        fields = ['titulo', 'responsavel', 'descricao', 'grau_urgencia']