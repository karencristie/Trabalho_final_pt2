# tarefas/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('minhas/', views.minhas_demandas, name='minhas_demandas'),
    path('registrar/', views.registrar_usuario, name='registrar'),

    path('cadastrar/', views.cadastrar_demanda, name='cadastrar_demanda'),
    path('restrito/', views.lista_restrita, name='lista_restrita'),
    path('sucesso/', views.pagina_sucesso, name='pagina_sucesso'),
]