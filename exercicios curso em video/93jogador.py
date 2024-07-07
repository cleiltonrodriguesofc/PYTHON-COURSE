'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
 O programa vai ler o nome do jogador e quantas partidas ele jogou. 
 Depois vai ler a quantidade de gols feitos em cada partida. No final, 
 tudo isso será guardado em um dicionário, incluindo o total de gols feitos
durante o campeonato.'''
jogador = dict()
jogadores = []
while True:
    total_gols = []
    jogador['nome'] = input('Nome do jogador: ').strip().upper()
    jogador['numero de partidas'] = int(input('Número de partidas: '))
    for i in range(1, jogador['numero de partidas']+1):
        gols_partida = int(input(f'Número de gols na partida {i}: '))
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
for dado in jogadores:
    print(f'\n===== {dado['nome']} ======')
    print(f'PARTIDAS: {dado['numero de partidas']}')
    for i, gol in enumerate(dado['total_gols']):
        print(f'PARTIDA {i+1}: {gol} gols')
    print(f'{dado['nome']} fez {sum(dado['total_gols'])} gols no campeonato')
