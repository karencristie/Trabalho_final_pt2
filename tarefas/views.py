# tarefas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import DemandaForm
from .models import Demanda

# Função para checar se o usuário é Administrador (staff)
def is_admin(user):
    return user.is_staff

@login_required
def cadastrar_demanda(request):
    if request.method == 'POST':
        form = DemandaForm(request.POST)
        if form.is_valid():
            demanda = form.save(commit=False)
            demanda.solicitante = request.user # Associa o usuário logado
            demanda.save()
            return redirect('pagina_sucesso') # Redireciona para uma página de sucesso
    else:
        form = DemandaForm()
    
    return render(request, 'tarefas/cadastrar_demanda.html', {'form': form})

@login_required
@user_passes_test(is_admin) # Apenas usuários marcados como 'staff' podem acessar
def lista_restrita(request):
    # Busca todas as demandas, ordenadas pela data de criação mais recente
    todas_demandas = Demanda.objects.all().order_by('-data_criacao')
    return render(request, 'tarefas/lista_restrita.html', {'demandas': todas_demandas})

# Uma view simples para a página de sucesso
def pagina_sucesso(request):
    return render(request, 'tarefas/sucesso.html')