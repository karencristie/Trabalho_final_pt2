from django.db import models
from django.contrib.auth.models import User

# Opções para o grau de urgência
GRAU_URGENCIA_CHOICES = (
    ('B', 'Baixa'),
    ('M', 'Média'),
    ('A', 'Alta'),
)

class Demanda(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    grau_urgencia = models.CharField(max_length=1, choices=GRAU_URGENCIA_CHOICES)
    data_criacao = models.DateTimeField(auto_now_add=True)
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='demandas_criadas')

    def __str__(self):
        return self.titulo