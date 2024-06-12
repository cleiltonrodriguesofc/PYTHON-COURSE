'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma 
lista. No final, mostre:
A) Quantas pessoas foram cadastradas.

B) Uma listagem com as pessoas mais pesadas. 

C) Uma listagem com as pessoas mais leves.'''

people = list()
person_list = []
heavier = lighter = 0

while True:
    
    person_list.append(str(input('Enter the person name: ')))
    person_list.append(int(input('Enter the person weight: ')))
    if len(people) == 0:
        heavier = lighter = person_list[1]
    else:
        if person_list[1] > heavier:
            heavier = person_list[1]
        elif person_list[1] < lighter:
            lighter = person_list[1]

    people.append(person_list[:])
    person_list.clear()

    stop = 'N'
    while True:
        stop = input('Wanna continue?[Y/N] ').strip().upper()
        if stop == 'Y':
            break
        elif stop == 'N':
            break
        else:
            print('Invalid option! Try again.')
            continue
    if stop == 'N':
        break
print(f'There was indexed {len(people)} people.')
print(f'The biggest weight is {heavier} kg and this is ', end='')
for p in people:
    if p[1] == heavier:
        print(f' {p[0]},', end=' ')
print()
print(f'The smaller weight is {lighter} kg and this is ', end=' ')
for p in people:
    if p[1] == lighter:
        print(f'{p[0]},', end=' ')
print()