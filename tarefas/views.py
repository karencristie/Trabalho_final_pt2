# tarefas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import DemandaForm
from .models import Demanda
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Salva o novo usuário no banco de dados
            login(request, user) # Loga o usuário automaticamente após o cadastro
            return redirect('cadastrar_demanda') # Redireciona para a página de cadastro de tarefas
    else:
        form = UserCreationForm()
    return render(request, 'tarefas/registrar.html', {'form': form})

@login_required # Garante que o usuário esteja logado
def minhas_demandas(request):
    # Filtra as demandas para pegar apenas aquelas onde o 'solicitante' é o usuário logado
    demandas_do_usuario = Demanda.objects.filter(solicitante=request.user).order_by('-data_criacao')
    return render(request, 'tarefas/minhas_demandas.html', {'demandas': demandas_do_usuario})