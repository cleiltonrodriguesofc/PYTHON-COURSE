''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos. '''
import statistics
dict_info = {}
oldest_man_name = ''
max_age = 0
women_under_20 = 0
for i in range(1, 5):
    print('-='*10, f'{i}° PERSON.', '-='*10)
    name = str(input('NAME: ')).strip().upper()
    age = int(input('AGE: '))
    sex = str(input('SEX: ')).strip().upper()
    dict_info[name] = {'age': age, 'sex': sex}
    if sex == 'F' and age < 20:
        women_under_20 += 1
    elif sex == 'M' and age > max_age:
        oldest_man_name = name
        max_age = age
average_age = statistics.mean(info['age'] for info in dict_info.values())
print('-='*30)
print(f'THE AVERAGE AGE OF THE GROUP IS {average_age} YEARS OLD.')
print('-='*30)
print(f'THE OLDEST MAN IS {oldest_man_name} AND HE IS {max_age} YEARS OLD.')
print('-='*30)
print(f'THERE ARE {women_under_20} WOMAN UNDER  20 YEARS OLD.')