'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa 
vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para 
cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
import time
megasena = []
while True:
    quantjogos = int(input('Quantos jogos você quer? '))
    for h in range(1, quantjogos+1):
        jogos = []
        while len(jogos) < 6:
            gerar = randint(1, 60)
            if gerar not in jogos:
                jogos.append(gerar)
        if jogos not in megasena:
            megasena.append(jogos)
        else:
            continue
    break
print('Os jogos gerados são:')
for jogo in megasena:
    jogo.sort()
    print(*jogo)
    time.sleep(1)
print('Boa sorte!')