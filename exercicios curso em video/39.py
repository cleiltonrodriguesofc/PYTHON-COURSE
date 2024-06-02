'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar 
ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
born = int(input('Enter your born year: '))
age = 2024 - born
if age < 18:
    need = 18 - age
    print(f'You are {age} years old. You have no age to do military enlistment. You can do that in {need} years.')
else:
    need = age - 18
    print(f'You are {age} years old. You already should have to do your military enlistment {need} years ago.')
