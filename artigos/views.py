from django.shortcuts import render
from django.http import HttpResponse
import datetime

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
    return render(request,'artigos/modelagens/sistemas_rotacionais/pendulo_simples_lagrange.html')

def modelagem_pendulo_simples_newton(request):
    return render(request,'artigos/modelagens/sistemas_rotacionais/pendulo_simples_newton.html')

def modelagem_pendulo_conico_lagrange(request):
    return render(request,'artigos/modelagens/sistemas_rotacionais/pendulo_conico_lagrange.html')

def modelagem_pendulo_conico_newton(request):
    return render(request,'artigos/modelagens/sistemas_rotacionais/pendulo_conico_newton.html')

def modelagem_pendulo_duplo(request):
    return render(request,'artigos/modelagens/sistemas_rotacionais/pendulo_duplo.html')

def modelagem_2_pendulos_conectados_por_mola(request):
    return render(request,'artigos/modelagens/sistemas_rotacionais/2_pendulos_conectados_por_mola.html')