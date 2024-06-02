"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""
year = int(input('Enter a year: '))
if year % 4 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year.')