"""Desenvolva um programa que leia o comprimento de três retas 
e diga ao usuário se elas podem ou não formar um triângulo."""
print('-='*20)
line1 = float(input('Enter first segment: '))
line2 = float(input('Enter second segment: '))
line3 = float(input('Enter third segment: '))
if line1 < line2 + line3 and line2 < line1 + line3 and line3 < line2 + line1:
    print('It forms a triangle')
else:
    print("It doesn't form a triangle.")