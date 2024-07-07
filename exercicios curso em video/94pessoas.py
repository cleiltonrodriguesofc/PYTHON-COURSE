'''Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados.txt de cada pessoa em um dicionário e todos os dicionários
em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas ok
B) A média de idade ok
C) Uma lista com as mulheres ok
D) Uma lista de pessoas com idade acima da média ok'''
import statistics
import time
pessoas = {}
lis_pessoas = []
idades = []
mulheres = []
while True:
    print()
    pessoas['nome'] = str(input('Nome: ')).strip().upper()
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if pessoas['sexo'] in 'MF':
            break
    pessoas['idade'] = int(input('Idade: '))
    idades.append(pessoas['idade'])
    if pessoas['sexo'] == 'F':
            mulheres.append(pessoas.copy())
    lis_pessoas.append(pessoas.copy())
    while True:
        continar = input('Cadastrar mais?[S/N] ').strip().upper()
        if continar == 'S':
            break
        if continar == 'N':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida!')
    if continar == 'N':
        break
print(f'Foram cadastradas {len(lis_pessoas)} pessoas.')
print(f'A média de idade é {statistics.mean(idades)}')
print()
print(f'As mulheres são:')
for mulher in mulheres:
    time.sleep(1)
    print(f'====={mulher['nome']}=====')
    print(f'IDADE: {mulher['idade']}')
print()
print('As pessoas com idade acima da média são:')
for dado in lis_pessoas:
    if dado['idade'] > statistics.mean(idades):
        time.sleep(1)
        print(f'{dado['nome']}: {dado['idade']} anos.')
