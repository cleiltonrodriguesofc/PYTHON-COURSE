''' Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
how_many = int(input(f'How many value do you want to enter? '))
values = []
for i in range(1, how_many+1):
    value = int(input(f'Enter the {i}° value: '))
    if value in values:
        pass
    else:
        values.append(value)
values.sort()
print(f'The inserted values in the list are {values}')
