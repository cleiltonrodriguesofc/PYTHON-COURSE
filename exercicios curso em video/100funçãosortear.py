'''Faça um programa que tenha uma lista chamada números e duas funções 
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números 
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma 
entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep
def enfeite():
    print('-=-'*15)
def sortear(valores):
    enfeite()
    for _ in range(5):
        valor = randint(1, 100)
        valores.append(valor)
    print(f'Os valores 5 sorteados foram ', end='')
    for valor in valores:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
    print('FIM!')
    enfeite()
    print()

def somar(sorteados):
    enfeite()
    soma = sum(sorteado for sorteado in sorteados if sorteado % 2 == 0)
    print(f'A soma dos numeros pares sorteados é ', end='', flush=True)
    for _ in range(3):
        print(f'.', end=' ', flush=True)
        sleep(1)
    print(soma)
    enfeite()

# PROGRAMA PRINCIPAL
valores = []
sorteados = valores
sortear(valores)
somar(sorteados)