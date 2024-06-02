'''Desenvolva um programa que leia seis números 
inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.'''
pares = []
print('DIGITE SEIS NÚMEROS.')
print('-='*10)
for i in range(1, 7):
    num = int(input(f'DIGITE O {i}° NÚMERO: '))
    if num % 2 == 0:
        pares.append(num)
soma = sum(pares)
cont = len(pares)
print(f'VOCÊ INFORMOU {cont} NÚMEROS PARES.')
print(f'A SOMA DOS NÚMEROS PARES É {soma}')