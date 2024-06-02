'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantaspessoas ainda não atingiram a maioridade 
e quantas já são maiores.'''
import datetime
date = datetime.date.today()
act_year = date.year
dict_name = {}
for i in range(1, 3):
    name = input('ENTER YOUR NAME: ').upper()
    born_year = int(input('ENTER YOUR BORN YEAR: '))
    dict_name[name] = born_year
    print('*'*20)
for name, born_year in dict_name.items():
    age = act_year - born_year
    if age > 18:
        print(f'{name} IS {age} YEARS OLD. YOU HAVE REACHED ADULTHOOD')
        print('-'*20)    
    else:
        print(f'{name} IS {age} YEARS OLD. YOU HAVE NOT REACHED ADULTHOOD')
        print('-'*20)
