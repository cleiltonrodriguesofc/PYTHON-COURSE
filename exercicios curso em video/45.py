'''Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('VAMOS JOGAR!')
print(
'''
0. PEDRA
1. PAPEL
2. TESOURA
''')
pc = randint(0, 2)
while True:
    player = int(input('ESCOLHA UMA OPÇÃO: '))
    if 2 >= player >= 0:
        break
    else:
        print('OPÇÃO INVÁLIDA')
        
print('-=' * 15)
print(f'O COMPUTADOR ESCOLHEU {itens[pc]}')
print(f'VOCÊ ESCOLHEU {itens[player]}')
print('-=' * 15)
if pc == player:
    print('DEU EMPATE')
    print('-=' *15)
else:
    if pc == 0 and player == 2:
        print('COMPUTADOR VENCEU!')
        print('-=' *15)
    elif pc == 0 and player == 1:
        print('JOGADOR VENCEU!')
        print('-=' *15)
    elif pc == 2 and player == 1:
        print('COMPUTADOR VENCEU!')
        print('-=' *15)
    elif pc == 1 and player == 2:
        print('JOGADOR VENCEU!')
        print('-=' *15)
    elif pc == 1 and player == 0:
        print('COMPUTADOR VENCEU!')
        print('-=' *15)
    