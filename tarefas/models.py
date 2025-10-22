# tarefas/models.py
from django.db import models
from django.contrib.auth.models import User

# Opções para o grau de urgência
GRAU_URGENCIA_CHOICES = (
    ('B', 'Baixa'),
    ('M', 'Média'),
    ('A', 'Alta'),
)

# Opções de Status
STATUS_CHOICES = (
    ('PEN', 'Pendente'),
    ('AND', 'Em Andamento'),
    ('CON', 'Concluída'),
)

# --- 1. NOVO MODELO CRIADO AQUI ---
class Profissional(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
# ------------------------------------

class Demanda(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    
    # --- 2. CAMPO "RESPONSAVEL" MODIFICADO ---
    # Ele não é mais um ForeignKey para 'User', e sim para 'Profissional'
    responsavel = models.ForeignKey(Profissional, on_delete=models.SET_NULL, null=True, blank=True)
    # ----------------------------------------
    
    grau_urgencia = models.CharField(max_length=1, choices=GRAU_URGENCIA_CHOICES)
    data_criacao = models.DateTimeField(auto_now_add=True)
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='demandas_criadas')
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')

    def __str__(self):
        return self.titulo