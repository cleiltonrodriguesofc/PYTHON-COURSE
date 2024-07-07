'''Faça um programa que tenha uma função chamada área(), que receba as 
dimensões de um terreno retangular (largura e comprimento) e mostre a área 
do terreno.'''
def area(larg, comp):
    print('=-='*10)
    print(f'A área do terreno é {larg*comp} m².')
    print('=-='*10)

# PROGRAMA PRINCIPAL
larg = float(input('Digite a largura do terreno[m]: '))
comp = float(input('Digite o comprimento do terreno[m]: '))
area(larg, comp)