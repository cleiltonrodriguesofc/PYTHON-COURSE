'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado.'''
# jogadores: ANA, JORGE, MARIA E PEDRO
# DICIONÁRIO PARA VALORES DE CADA UM
from random import randint
import time
jogadores = {}
while True:
    print('Quem joga? Digite "P" para parar.')
    print('|--ANA\n|--JORGE\n|--MARIA\n|--PEDRO')
    while True:
        escolherjogador = str(input('Digite o nome do jogador: ')).strip().upper()
        if escolherjogador == 'ANA':
            pc = randint(1, 6)
            jogadores['ANA'] = pc
            break
        if escolherjogador == 'JORGE':
            pc = randint(1, 6)
            jogadores['JORGE'] = pc
            break
        if escolherjogador == 'MARIA':
            pc = randint(1, 6)
            jogadores['MARIA'] = pc
            break
        if escolherjogador == 'PEDRO':
            pc = randint(1, 6)
            jogadores['PEDRO'] = pc
            break
        if escolherjogador == 'P':
            print('Saindo do Jogo...\n')
            break
        else:
             print('Opção inválida!')
    if escolherjogador == 'P':
            break

jogadores_ord = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
for k, v in jogadores_ord:
     print('-'*20)
     time.sleep(1)
     print(f'{k} tirou {v}')
print('=-='*8)
chave_maior_valor = max(jogadores, key=jogadores.get)
print(f'{chave_maior_valor} tirou {jogadores[chave_maior_valor]} e VENCEU')