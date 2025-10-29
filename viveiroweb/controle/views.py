from statistics import quantiles


from django.shortcuts import redirect, render , get_list_or_404
#from django.contrib.auth.decorators import login_required // isso vai dizer que a rota só pode ser acessada por usuários logados
from .models import Planta, Reserva, AcaoEnsino
from django.http import JsonResponse

# Create your views here.

def home(request):
    plantas_aleatorias = Planta.objects.order_by('?')[:12]
    return render(request, 'home.html', {'plantas': plantas_aleatorias})

def formulario_uso_viveiro(request):
    return render(request, 'formulario_uso_viveiro.html')

def pesquisa_extensao(request):
    acoes = AcaoEnsino.objects.filter(aceito=True)

    # Seleciona 12 aleatórias
    acoes_aleatorias = acoes.order_by('?')[:12]
    return render(request, 'pesquisa_extensao.html', {'acoes': acoes, 'acoes_aleatorias': acoes_aleatorias})

def sobre(request):
    return render(request, 'sobreNos.html')


def enviar_reserva(request):
    if request.method == 'GET':
        nome = request.GET.get('nome')
        email = request.GET.get('email')
        telefone = request.GET.get('telefone')
        data = request.GET.get('data')
        motivo = request.GET.get('motivo')
        descricao = request.GET.get('descricao')
# Cria e salva a reserva
        Reserva.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            data=data,
            motivo=motivo,
            descricao=descricao
        )
        # Redireciona ou renderiza uma página de sucesso
        return render(request, 'formulario_uso_viveiro.html', {'mensagem': 'Reserva enviada com sucesso!'})

def enviar_acao(request):
    if request.method == 'GET':
        tipo = request.GET.get('tipo')
        nome = request.GET.get('nome')
        descricao = request.GET.get('descricao')
        autores = request.GET.get('autores')
        # Cria e salva a ação
        AcaoEnsino.objects.create(
           
            tipo=tipo,
            nome=nome,
            autores=autores,
            descricao=descricao
        )
        # Redireciona ou renderiza uma página de sucesso
        return redirect('pesquisa_extensao')  # use o nome da sua URL

def dias_ocupados(request):
    pendentes = Reserva.objects.filter(aceito=False).values_list("data", flat=True)
    aprovados = Reserva.objects.filter(aceito=True).values_list("data", flat=True)

    return JsonResponse({
        "pendentes": [d.strftime("%Y-%m-%d") for d in pendentes],
        "aprovados": [d.strftime("%Y-%m-%d") for d in aprovados],
    })


def catalogo(request):
    plantas= Planta.objects.order_by('nome')
    plantas_tamanho = len(plantas)
    return render(request, 'catalogo.html', {'plantas': plantas, 'plantas_tamanho': plantas_tamanho})

def pesquisar(request):
    pesquisa = request.GET.get('pesquisa')
    if pesquisa:
        resultados = Planta.objects.filter(nome__icontains=pesquisa)
        quantidade = len(resultados)
    else:
        resultados = Planta.objects.all()
        quantidade = len(resultados)

    return render(request, 'pesquisa.html', {'resultados': resultados, 'quantidade': quantidade})