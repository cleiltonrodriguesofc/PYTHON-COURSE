'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será 
interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que 
ele conquistou no final do jogo.'''
from random import randint
print('='*20)
print('=JOGO PAR OU IMPAR=')
print('='*20)
while True:
    jogador = int(input('Diga um valor: '))
    pc = randint(1, 10)
    soma = jogador + pc
    escolha = ' '
    ganhojodador = 0
    
    while escolha not in 'PI':
        escolha = input('Par ou Impar? ').upper().strip()[0]
    if escolha == 'P':
        if soma % 2 == 0:
            print(f'Computador colocou {pc} e jogador colocou {jogador}')
            print(f'A soma deu {soma} que é PAR')
            print('='*20)
            print('==Jogador ganhou==!')
            ganhojodador += 1
        elif soma % 2 == 1:
            print(f'Computador colocou {pc} e jogador colocou {jogador}')
            print(f'A soma deu {soma} que é IMPAR')
            print('='*20)
            print('==Jogador perdeu==!')
            break
    
    elif escolha == 'I':
        if soma % 2 == 0:
            print(f'Computador colocou {pc} e jogador colocou {jogador}')
            print(f'A soma deu {soma} que é PAR')
            print('='*20)
            print('==Jogador perdeu!==')
            break
        
        elif soma % 2 == 1:
            print(f'Computador colocou {pc} e jogador colocou {jogador}')
            print(f'A soma deu {soma} que é IMPAR')
            print('='*20)
            print('==Jogador ganhou!==')
            ganhojodador += 1
    print('='*20)
    print('Vamos jogar novamente...!')
    print('='*20)