from django.urls import path
from artigos import views

urlpatterns = [
    path('', views.home, name='home'),
    path('animacoes/', views.animacoes, name='animacoes'),
    path('roteador/', views.roteador, name='roteador'),
    path('sistema_detalhes/', views.sistema_detalhes, name='sistema_detalhes'),
    path('sobre/contato/', views.contato, name='contato'),
    path('sobre/doacoes/', views.doacoes, name='doacoes'),
    path('sobre/parceiros/', views.parceiros, name='parceiros'),
    path('sobre/quem_somos/', views.quem_somos, name='quem_somos'),
    path('animacoes/animacao_pendulo_simples/', views.animacao_pendulo_simples, name='animacao_pendulo_simples'),
]