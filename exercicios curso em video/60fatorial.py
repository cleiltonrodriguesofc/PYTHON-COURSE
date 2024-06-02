''' Faça um programa que leia um número qualquer e mostre o seu fatorial. 
Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120'''
from math import factorial
number = int(input('ENTER A NUMBER: '))
print(f'CALCULING {number}! = ', end='')
n = number
while True:
    if number > 0:
        print(f'{n}', end='')
        print(f' x ' if n > 1 else ' = ', end='')
        n -= 1
        if n == 0:
            break
fat = factorial(number)
print(fat)