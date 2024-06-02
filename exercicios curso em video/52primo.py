'''Faça um programa que leia um número inteiro 
e diga se ele é ou não um número primo.'''

num = int(input('DIGITE UM NÚMERO INTEIRO: '))
divisores = []
for i in range(1, num + 1):
    if num % i == 0:
        divisores.append(i)
cont_divisores = len(divisores)
# verificar se é primo
if cont_divisores == 2:
    print(f'O NÚMERO {num} É UM NÚMERO PRIMO.')
else:
    print(f'O NÚMERO {num} NÃO É UM NÚMERO PRIMO.')