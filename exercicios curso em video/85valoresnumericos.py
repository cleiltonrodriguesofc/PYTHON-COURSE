'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os 
em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre
os valores pares e ímpares em ordem crescente.'''

values = [[], []]

print('ENTER 7 VALUES')
for i in range(1, 8):
    value = int(input(f'Enter the {i}° value: '))
    if value % 2 == 0:
        values[0].append(value)
    else:
        values[1].append(value)

values[0].sort() #ordenar pares
print(f'The even values are {values[0]}.')
values[1].sort() #ordenar impares
print(f'The odd values are {values[1]}.')
