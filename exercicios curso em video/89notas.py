'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em 
uma lista composta. No final, mostre um boletim contendo a média de cada um e 
permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
import statistics   
boletim = list()
while True:
    aluno_e_nota = []
    aluno_e_nota.append(str(input('Aluno: ')).strip().upper())
    aluno_e_nota.append(int(input('Nota 1: ')))
    aluno_e_nota.append(int(input('Nota 2: ')))
    media = statistics.mean(aluno_e_nota[1:3])
    aluno_e_nota.append(media)
    boletim.append(aluno_e_nota)
    parar = 'n'
    while True:
        continuar = input('Quer continuar? ').strip().lower()
        if continuar == 's':
            break
        if continuar == 'n':
            break
        else:
            print('Opção inválida!')
    if continuar == 'n':
            break
for aluno, nota1, nota2, media in boletim:
     print('=-='*4)
     print(f'=== {aluno} ===\nNOTA 1: {nota1:.2f}\nNOTA 2: {nota2:.2f}\nMÉDIA: {media:.2f}')
     print('=-='*4)