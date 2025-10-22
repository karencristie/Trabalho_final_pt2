# tarefas/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('minhas/', views.minhas_demandas, name='minhas_demandas'),
    path('registrar/', views.registrar_usuario, name='registrar'),

    path('cadastrar/', views.cadastrar_demanda, name='cadastrar_demanda'),
    path('restrito/', views.lista_restrita, name='lista_restrita'),
    path('sucesso/', views.pagina_sucesso, name='pagina_sucesso'),

    path('demanda/<int:demanda_id>/andamento/', views.marcar_em_andamento, name='marcar_andamento'),
    path('demanda/<int:demanda_id>/concluida/', views.marcar_concluida, name='marcar_concluida'),
    path('demanda/<int:demanda_id>/excluir/', views.excluir_demanda, name='excluir_demanda'),
]