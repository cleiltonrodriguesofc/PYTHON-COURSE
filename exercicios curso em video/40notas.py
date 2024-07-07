'''Crie um programa que leia duas notas de um aluno e calcule sua média, 
mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''
print('Enter your grades')
grade1 = float(input('Enter your first-grade: '))
grade2 = float(input('Enter your second-grade: '))

average = (grade1 + grade2) / 2

if average < 5:
    print(f'Your average is {average}. YOU ARE REPROVAD.')
elif average <= 6.99 and average > 5:
    print(f'Your average is {average}. You have to do RECUPERATION.')
else:
    print(f'Your average is {average}. CONGRATULATIONS! You are APROVAD.')
