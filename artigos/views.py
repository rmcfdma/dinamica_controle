from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator,InvalidPage
import json,os
from pathlib import Path as p

ITEMS_PER_PAGE = 1
BASE_DIR = p(__file__).resolve().parent.parent
path = os.path.join(BASE_DIR,'artigos/static/artigos/json/')

def jsonToDict(sistema):
    caminho = os.path.join(path , sistema)
    with  open(caminho, 'r', encoding="utf-8") as f:
        dicionario = json.load(f)
    return dicionario

# Gera uma lista de cada sistema [id, nome]
def getSistemas():
    dicionario = jsonToDict('sistemas.json')
    sistemas = []
    for key,value in dicionario.items():
        sistemas.append([value['id'], key])
    return sistemas

def home(request):
    context = {'sistemas':getSistemas()}
    return render(request,'artigos/home.html',context)

def roteador(request):
    # Recupera os dados do dicionário
    dicionario = jsonToDict('sistemas.json')
    # Recupera a página atual do paginator, que neste
    # caso só possui 1 elemento conforme ITEMS_PER_PAGE.
    page = request.GET.get('page', 1) # Ex. Pêndulo Simples - Lagrange
    # Busca no dicionario os valores do sistema, do subsistema
    # e do tipo com os valores passados na requisição e, 
    # caso não encontre, retorna 'Mecânicos'.
    system = dicionario[request.GET.get('name', 'Mecânicos')]
    subsystem = system[request.GET.get('subsistema', 'Rotacionais')]
    tipo = subsystem[request.GET.get('tipo', 'Pêndulos')]
    # Pesquisa os diretórios dos referidos sistema e subsistema.
    system_url = system['url'][1]  # Ex. sistemas_mecanicos/
    subsystem_url = subsystem['url'][1] # Ex. sistemas_mecanicos_rotacionais/
    # Envia para o treeview através do response o sistema, subsistema e o tipo.
    url = [request.GET.get('name', 'Mecânicos'),request.GET.get('subsistema', 'Rotacionais'),request.GET.get('tipo', 'Pêndulos')]
    # Cria e popula a lista que conterá os modelos
    lista = []
    for k in tipo:
        for n in k[2]:
            lista.append(n)    
    # Cria um paginator com a lista de modelos criando n sublistas
    # com cada sublista contedo ITEMS_PER_PAGE de forma que se 
    # a lista contém 20 registros e queremos apresentar 4 registros por página
    # teremos 20/4 = 5 sublistas. Nesse caso cada página contém apenas 1 registro (modelo).
    paginator = Paginator(lista, ITEMS_PER_PAGE)
    # Númeri de sublistas
    total = paginator.count
    try:
        # Tenta, através da página atual, retornar o índice da próxima página.
        paginas = paginator.page(page)
    except InvalidPage:
        # No caso de haver algum problema retorna a sublista 1.
        paginas = paginator.page(1)
    # Dicionário a ser enviado no response, onde:
    # paginas: Indice da próxima sublista a ser apresentada (utilizada no menu paginator)
    # total: total de páginas
    # lista: Modelos a serem apresentados
    # sistemas: Nome dos sistemas apresentados no accordion
    # url: Nomes d sistema, subsistema e tipo a serem retornados
    # pelo paginator que irão servir de keys no próximo request para
    # localizar os diretórios corretos. 
    context = {'paginas': paginas, 'total': total, 'lista': lista,'sistemas':getSistemas(),'url':url}
    return render(request,'artigos/modelagens/'+ system_url + subsystem_url + lista[int(page)-1][2],context)

# Método utilizado para listar os subsistemas
# e modelos através do accordion.
def sistema_detalhes(request):
    # Recupera o id do sistema embutido na requisição
    id = request.GET.get('id', 1) 
    # Carrega o dicionário
    dicionario = jsonToDict('sistemas.json')
    # Carrega uma lista com o id e respectivo nome dos sitemas
    sistemas = getSistemas()
    # Cria uma variável para armazenar o nome do sistema corrente
    name = 'qualquer'
    # Loopa sobre os sistemas no dicionario
    for key,value in dicionario.items():
        # Compara o id vindo do template com os id's dos sistemas
        if str(value['id']) == id:
            # Caso seja igual pega o nome do sistema
            name = key
    # Seleciona o sistema correto baseado no nome encontrado
    subsistemas = dicionario[name]
    # Encapsula os dados em um dicionário a ser enviados no response
    # 'sistemas' para o accordion
    # 'Name' para o título
    # 'subsistemas' para o treeview
    context = {'sistemas': sistemas, 'name':name, 'subsistemas':subsistemas}
    return render(request,'artigos/modelagens/sistemas.html',context)


def animacoes(request):
    return render(request,'artigos/animacoes/animacoes.html')

def animacao_pendulo_simples(request):
    return render(request,'artigos/animacoes/animacao_pendulo_simples.html')

def modelagem_pendulo_duplo(request):
    return render(request,'artigos/modelagens/sistemas_rotacionais/pendulo_duplo.html')

def doacoes(request):
    context = {'sistemas':getSistemas()}
    return render(request,'artigos/sobre/doacoes.html',context)

def contato(request):
    context = {'sistemas':getSistemas()}
    return render(request,'artigos/sobre/contato.html',context)

def parceiros(request):
    context = {'sistemas':getSistemas()}
    return render(request,'artigos/sobre/parceiros.html',context)

def quem_somos(request):
    context = {'sistemas':getSistemas()}
    return render(request,'artigos/sobre/quem_somos.html',context)