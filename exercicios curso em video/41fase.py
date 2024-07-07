'''A Confederação Nacional de Natação precisa de um programa que leia 
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''
at = int(input('Enter your born year: '))
age = 2024 - at
if age <= 9:
    print('YOU ARE CHILD.')
elif age <= 14 and age > 9:
    print('YOU ARE INFANTILE.')
elif age <= 19 and age > 14:
    print('YOU ARE JUNIOR.')
elif age <= 25 and age > 19:
    print('YOU ARE A SENIOR.')
else:
    print('YOU ARE MASTER.')