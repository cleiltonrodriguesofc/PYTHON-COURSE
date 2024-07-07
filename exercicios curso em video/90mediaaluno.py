'''Faça um programa que leia nome e média de um aluno, guardando também a situação 
em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''
import time
boletim = {}
alunos = []
while True:
    boletim['aluno'] = input('Nome do aluno: ').upper()
    boletim['nota1'] = int(input('Nota 1: '))
    boletim['nota2'] = int(input('Nota 2: '))
    boletim['media'] = (boletim['nota1'] + boletim['nota2']) / 2
    if boletim['media'] >= 7:
        boletim['situacao'] = 'APROVADO'
    else:
        boletim['situacao'] = 'REPROVADO'
    alunos.append(boletim.copy())
    while True:
        continuar = input('Quer Cadastrar mais alunos?[S/N] ').strip().upper() 
        if continuar == 'S':
            break
        if continuar == 'N':
            break
        else:
            print('Opção inválida!')
    if continuar == 'N':
        break
for aluno in alunos:
    time.sleep(1)
    print('\n==  BOLETIM  ==')
    time.sleep(1)
    print(f'ALUNO: {aluno['aluno']}')
    time.sleep(1)
    print(f'NOTA 1: {aluno['nota1']}')
    time.sleep(1)
    print(f'NOTA 2: {aluno['nota2']}')
    time.sleep(1)
    print(f'MÉDIA: {aluno['media']}')
    time.sleep(1)
    print(f'SITUAÇÃO: {aluno['situacao']}')