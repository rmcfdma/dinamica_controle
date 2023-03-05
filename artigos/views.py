from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator,InvalidPage
import json,os
from pathlib import Path as p

ITEMS_PER_PAGE = 1
BASE_DIR = p(__file__).resolve().parent.parent
path = os.path.join(BASE_DIR,'artigos/static/artigos/json/')

# lista = [
#    (1, "modelagem_pendulo_simples_lagrange", "pendulo_simples_lagrange.html"),
#    (2, "modelagem_pendulo_simples_newton", "pendulo_simples_newton.html"),
#    (3, "modelagem_pendulo_conico_lagrange", "pendulo_conico_lagrange.html"),
#    (4, "modelagem_pendulo_conico_newton", "pendulo_conico_newton.html")
# ]

def jsonToDict(sistema):
    caminho = os.path.join(path , sistema)
    with  open(caminho, 'r') as f:
        dicionario = json.load(f)
    return dicionario


def router(request):
    page = request.GET.get('page', 1)
    tuplas = tuple(jsonToDict('sistemas_rotacionais.json'))
    paginator = Paginator(tuplas, ITEMS_PER_PAGE)
    total = paginator.count
    try:
        paginas = paginator.page(page)
    except InvalidPage:
        paginas = paginator.page(1)
    context = {'paginas': paginas,'total': total}
    return render('artigos/modelagens/sistemas_rotacionais/' + tuplas[int(page)-1][2],context)
   

def home(request):
    return render(request,'artigos/home.html')

def animacoes(request):
    return render(request,'artigos/animacoes/animacoes.html')

def animacao_pendulo_simples(request):
    return render(request,'artigos/animacoes/animacao_pendulo_simples.html')

def modelagem_sistemas_translacionais(request):
    return render(request,'artigos/modelagens/sistemas_translacionais.html')

def modelagem_sistemas_rotacionais(request):
    return render(request,'artigos/modelagens/sistemas_rotacionais.html')

def modelagem_sistemas_hibridos(request):
    return render(request,'artigos/modelagens/sistemas_hibridos.html')

def modelagem_pendulo_simples_lagrange(request):
    page = request.GET.get('page', 1)
    tuplas = tuple(jsonToDict('sistemas_rotacionais.json'))
    paginator = Paginator(tuplas, ITEMS_PER_PAGE)
    total = paginator.count
    try:
        paginas = paginator.page(page)
    except InvalidPage:
        paginas = paginator.page(1)
    context = {'paginas': paginas, 'total': total}
    return render(request,'artigos/modelagens/sistemas_rotacionais/' + tuplas[int(page)-1][2],context)

def modelagem_pendulo_simples_newton(request):
    page = request.GET.get('page', 1)
    tuplas = tuple(jsonToDict('sistemas_rotacionais.json'))
    paginator = Paginator(tuplas, ITEMS_PER_PAGE)
    total = paginator.count
    try:
        paginas = paginator.page(page)
    except InvalidPage:
        paginas = paginator.page(1)
    context = {'paginas': paginas, 'total': total}
    return render(request,'artigos/modelagens/sistemas_rotacionais/' + tuplas[int(page)-1][2],context)

def modelagem_pendulo_conico_lagrange(request):
    page = request.GET.get('page', 1)
    tuplas = tuple(jsonToDict('sistemas_rotacionais.json'))
    paginator = Paginator(tuplas, ITEMS_PER_PAGE)
    total = paginator.count
    try:
        paginas = paginator.page(page)
    except InvalidPage:
        paginas = paginator.page(1)
    context = {'paginas': paginas, 'total': total}
    return render(request,'artigos/modelagens/sistemas_rotacionais/' + tuplas[int(page)-1][2],context)

def modelagem_pendulo_conico_newton(request):
    page = request.GET.get('page', 1)
    tuplas = tuple(jsonToDict('sistemas_rotacionais.json'))
    paginator = Paginator(tuplas, ITEMS_PER_PAGE)
    total = paginator.count
    try:
        paginas = paginator.page(page)
    except InvalidPage:
        paginas = paginator.page(1)
    context = {'paginas': paginas, 'total': total}
    return render(request,'artigos/modelagens/sistemas_rotacionais/' + tuplas[int(page)-1][2],context)

def modelagem_pendulo_duplo(request):
    return render(request,'artigos/modelagens/sistemas_rotacionais/pendulo_duplo.html')

def modelagem_2_pendulos_conectados_por_mola(request):
    return render(request,'artigos/modelagens/sistemas_rotacionais/2_pendulos_conectados_por_mola.html')

def doacoes(request):
    return render(request,'artigos/sobre/doacoes.html')

def contato(request):
    return render(request,'artigos/sobre/contato.html')

def parceiros(request):
    return render(request,'artigos/sobre/parceiros.html')

def quem_somos(request):
    return render(request,'artigos/sobre/quem_somos.html')