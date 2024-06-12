'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
crie duas listas extras que vão conter apenas os valores pares e os valores ímpares 
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
allvalues = list()
evenvalues = list()
oddvalues = list()
while True:
    value = int(input(f'Enter a value: '))
    allvalues.append(value)
    if value % 2 == 0:
        evenvalues.append(value)
    elif value % 2 == 1:
        oddvalues.append(value)
    cont = 'Y'
    while cont == 'Y':
        cont = input('Do you want to continue?[Y/N] ').strip().upper()
        if cont == 'Y':
            break
        elif cont == 'N':
            break
        else:
            print('Invalid option! Try again.')
    if cont == 'N':
        break

print(f'\nThe entered values are ', end=' ')
print(*allvalues)
print(f'\nThe even values are: ', end=' ')
print(*evenvalues)
print(f'\nThe odd values are ', end=' ')
print(*oddvalues)