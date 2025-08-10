from django.shortcuts import render
from .models import Planta

# Create your views here.

def home(request):
    plantas_aleatorias = Planta.objects.order_by('?')[:12]
    return render(request, 'home.html', {'plantas': plantas_aleatorias})

def catalogo(request):
    plantas= Planta.objects.order_by('nome')
    plantas_tamanho = len(plantas)
    return render(request, 'catalogo.html', {'plantas': plantas, 'plantas_tamanho': plantas_tamanho})