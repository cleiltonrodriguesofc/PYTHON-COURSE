'''Crie um programa onde o usuário possa digitar cinco valores numéricos e 
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.'''
values = []
for i in range(1, 6):
    value = int(input(f'Enter the {i}° value: '))
    if i == 1 or value > values[-1]:
        values.append(value)
        print('Value entered in the end list')
    else:
        position = 0
        while position < len(values):
            if value <= values[position]:
                values.insert(position, value)
                print(f'Value entered in the position {position} of the list.')
                break
            position += 1
print('=-='*15)
print(f'The entered values are: {values}')
