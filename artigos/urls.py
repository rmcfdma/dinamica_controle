from django.urls import path
from artigos import views

urlpatterns = [
    path('', views.home, name='home'),
    path('animacoes/', views.animacoes, name='animacoes'),
    path('animacoes/animacao_pendulo_simples/', views.animacao_pendulo_simples, name='animacao_pendulo_simples'),
    path('modelagem/sistemas_translacionais/', views.modelagem_sistemas_translacionais, name='modelagem_sistemas_translacionais'),
    path('modelagem/sistemas_rotacionais/', views.modelagem_sistemas_rotacionais, name='modelagem_sistemas_rotacionais'),
    path('modelagem/sistemas_hibridos/', views.modelagem_sistemas_hibridos, name='modelagem_sistemas_hibridos'),
    path('modelagem/pendulo_simples_lagrange/', views.modelagem_pendulo_simples_lagrange, name='modelagem_pendulo_simples_lagrange'),
    path('modelagem/pendulo_simples_newton/', views.modelagem_pendulo_simples_newton, name='modelagem_pendulo_simples_newton'),
    path('modelagem/pendulo_conico_lagrange/', views.modelagem_pendulo_conico_lagrange, name='modelagem_pendulo_conico_lagrange'),
    path('modelagem/pendulo_conico_newton/', views.modelagem_pendulo_conico_newton, name='modelagem_pendulo_conico_newton'),
    path('modelagem/pendulo_duplo/', views.modelagem_pendulo_duplo, name='modelagem_pendulo_duplo'),
    path('modelagem/2_pendulos_conectados_por_mola/', views.modelagem_2_pendulos_conectados_por_mola, name='modelagem_2_pendulos_conectados_por_mola'),
]