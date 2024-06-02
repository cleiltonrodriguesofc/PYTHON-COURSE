'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''
# ENTRAR PRIMEIRO TERMO
p1 = int(input('DIGITE O PRIMEIRO TERMO DA PROGRESSÃO ARITMÉTICA: '))
# ENTRAR RAZAO
r = int(input('DIGITE A RAZÃO DA PROGRESSÃO ARITMÉTICA: '))
# CRIAR LISTA PARA TERMOS
listapa = []
# DEFINIR FORMULA DE CALCULO
for i in range(2, 11):
    an = p1 + (i - 1) * r
    # COLOCAR NUMEROS NUMA LISTA
    listapa.append(an)
# IMPRIMIR NÚMEROS
print('OS 10 NÚMEROS DA PROGRESSÃO ARITMÉTICA SÃO:')
print(p1, *listapa)