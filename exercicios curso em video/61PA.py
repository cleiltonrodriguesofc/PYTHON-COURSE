'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''
import time
p1 = int(input('ENTER THE FIRST TERM: '))
r = int(input('ENTER THE AP RAZON: '))
counter = 1
term = p1
while counter <= 10:
    print(f'{term} -> ', end='')
    term += r
    counter += 1
print('FIM')