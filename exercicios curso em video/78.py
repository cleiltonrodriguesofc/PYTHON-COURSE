'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
 mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na 
 lista.'''
values = []
print('ENTER 5 VALUES')
for value in range(1, 6):
    value = int(input(f'Enter the {value}° value: '))
    values.append(value)
print(f'The biggest entered values is {max(values)} and it is in the position ', end='')
for position, value in enumerate(values):
    if value == max(values):
        print(f'{position+1}--', end=' ')
print()
print(f'The smaller entered value is {min(values)} and it is in the position ', end='')
for position, value in enumerate(values):
    if value == min(values):
        print(f'{position+1}--', end=' ')
        

