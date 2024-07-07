'''Faça um programa que tenha uma função chamada contador(), que receba 
três parâmetros: início, fim e passo. Seu programa tem que realizar três 
contagens através da função criada:
a) de 1 até 10, de 1 em 1 
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
import time
def enfeite():
    print(f'=-='*12)
def contador(inicio, fim, passo):
    print()
    enfeite()
    print(f'Contagem de {inicio} a {fim}, de {passo} em {passo}.')
    enfeite()
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont += passo
    if inicio > fim:
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            time.sleep(0.5)
            cont -= passo
    print('ACABOU!')
contador(1, 10, 1)
contador(10, 0, 2)

# função principal
print()
enfeite()
print('Agora é sua vez!')
enfeite()
ini = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(ini, f, p)