"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""
num = int(input('Enter a intire number: '))
if num % 2 == 0:
    print(f'The number {num} is a even number.')
else:
    print(f'The number {num} is a odd number.')