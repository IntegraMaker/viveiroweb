from django.shortcuts import render , get_list_or_404 
#from django.contrib.auth.decorators import login_required // isso vai dizer que a rota só pode ser acessada por usuários logados
from .models import Planta


# Create your views here.

def home(request):
    plantas_aleatorias = Planta.objects.order_by('?')[:12]
    return render(request, 'home.html', {'plantas': plantas_aleatorias})

def formulario_uso_viveiro(request):
    return render(request, 'formulario_uso_viveiro.html')

def enviar_reserva(request):
    if request.method == 'GET':
        nome = request.GET.get('nome')
        email = request.GET.get('email')
        telefone = request.GET.get('telefone')
        data = request.GET.get('data')
        motivo = request.GET.get('motivo')

def catalogo(request):
    plantas= Planta.objects.order_by('nome')
    plantas_tamanho = len(plantas)
    return render(request, 'catalogo.html', {'plantas': plantas, 'plantas_tamanho': plantas_tamanho})