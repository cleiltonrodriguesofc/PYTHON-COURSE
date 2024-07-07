'''Faça um programa que tenha uma função chamada ficha(), que receba dois 
parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum 
dado não tenha sido informado corretamente.'''
def enfeite():
    '''Função para imprimir enfeite'''
    print('=-='*15)


def ficha(nome='', gols=''):
    '''Função para imprimir nome e quantidade de gols
    nome = recebe qualquer valor, se não for um nome válido, retorna desconhecido
    gols = recebe qualquer valor, se não for um número, retorna desconhecido'''
    if nome == '' or nome.isnumeric():
        nome = 'desconhecido'
  
    if  gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    
    enfeite()
    print(f'JOGADOR: {nome}')
    print(f'GOLS: {gols}')
    enfeite()
    


# programa principal
n = input('Nome do jogador: ')
g = str(input('Quantos gols? '))
ficha(n, g)