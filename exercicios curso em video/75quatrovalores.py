'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma 
tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''
values = (int(input('Enter a value: ')), int(input('Enter a value: ')), int(input('Enter a value: ')), int(input('Enter a value: ')))
print(f'The value 9 appeared {values.count(9)} times.')
if 3 in values:
    print(f'The value 3 was entered in {values.index(3)+1}° position.')
else:
    print('Value 3 had no entered.')

print(f'The even values are ', end='')
for value in values:
    if value % 2 == 0:
        print(value, end=' ')