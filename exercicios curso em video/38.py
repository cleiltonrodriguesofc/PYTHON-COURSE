"""Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais"""
print('ENTER 2 INTIRE NUMBERS: ')
number1 = int(input(f'Enter the 1° number: '))
number2 = int(input(f'Enter the 2° number: '))
if number1 > number2:
    print(f'The first number is BIGGER.')
elif number2 > number1:
    print(f'The second number is BIGGER.')
else:
    print(f'The 2 number are EQUALS.')