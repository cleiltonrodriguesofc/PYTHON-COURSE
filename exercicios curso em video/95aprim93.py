''' Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada 
jogador.'''
jogador = dict()
jogadores = []
while True:
    total_gols = []
    jogador['nome'] = input('Jogador: ').strip().upper()
    jogador['numero de partidas'] = int(input('Partidas: '))
    for i in range(1, jogador['numero de partidas']+1):
        gols_partida = int(input(f'Gols na partida {i}: '))
        total_gols.append(gols_partida)
    jogador['total_gols'] = total_gols
    jogadores.append(jogador.copy())
    while True:
        continuar = input('Inserir outro jogador?[S/N] ').strip().upper()
        if continuar == 'S':
            break
        if continuar == 'N':
            break
        else:
            print('Opção inválida!')
    if continuar == 'N':
        break
print(jogadores)
while True:
    for i, dado in enumerate(jogadores):
        print(f'{i+1}   {dado['nome']}')
    while True:
        escolha = int(input('Digite o número do jogador [999 para sair]: '))
        if escolha == 999:
            print('Saindo do programa...')
            break
        if escolha > len(jogadores) or escolha == 0: 
            print('Opção inválida!')
        for i, dado in enumerate(jogadores):
            if escolha == i+1:
                print(f'\n===== {dado['nome']} ======')
                print(f'PARTIDAS: {dado['numero de partidas']}')
                for i, gol in enumerate(dado['total_gols']):
                    print(f'PARTIDA {i+1}: {gol} gols')
                print(f'{dado['nome']} fez {sum(dado['total_gols'])} gols no campeonato')
                break
    if escolha == 999:
        break

