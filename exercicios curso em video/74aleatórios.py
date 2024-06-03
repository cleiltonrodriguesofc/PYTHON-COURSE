'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior 
valor que estão na tupla.'''
from random import randint
n_randons = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'The generated numbers are ', end='')
print(*n_randons)
print(f'The biggest number is {max(n_randons)}.')
print(f'The smaller number is {min(n_randons)}.')