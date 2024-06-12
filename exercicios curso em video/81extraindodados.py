''' Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:

A) Quantos números foram digitados.

B) A lista de valores, ordenada de forma decrescente. 

C) Se o valor 5 foi digitado e está ou não na lista.'''
print('ENTER SOME VALUES.')
values = []
while True:
    value = int(input(f'Enter a number: '))
    values.append(value)
    while True:
        cont = input('Do you want to continue?[Y/N] ').strip().upper()
        if cont == 'Y':
            break
        if cont == 'N':
            break
        else:
            print('Invalid option!')
    if cont == 'N':
        break
# show how many number was entered
print(f'It was entered {len(values)} numbers.')
values.sort(reverse=True)
print(f'The values list in descending order is:', end=' ')
print(*values)
if 5 in values:
    print(f'The value 5 is in the list in the position {values.index(5)}')
else:
    print(f'The value 5 was no entered.')