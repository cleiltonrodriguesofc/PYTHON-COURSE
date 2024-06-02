'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint
pc = randint(0, 10)
counter_player = 0
while True:
    player = int(input('ENTER A NUMBER: '))
    counter_player += 1
    if player == pc:
        print(f'YOU WIN IN {counter_player} TENTATIVES, I THOUGHT IN {pc}')
        break
    else:
        if player < pc:
            print('MORE...! TRY AGAIN!')
        else:
            print('LESS...! TRY AGAIN!')
        