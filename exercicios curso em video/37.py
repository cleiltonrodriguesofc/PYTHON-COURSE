"""Escreva um programa em Python que leia um número inteiro qualquer e 
peça para o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal."""
number = int(input('Enter a intire number: '))

print("""CHOICE A CONVERTION FORM:
      1. BINÁRIO
      2. OCTAL
      3. HEXADECIMAL""")
while True:
    choice = int(input('Enter a NUMBER: '))
    if choice == 1:
        print(f'The number {number} in binary is {bin(number)}.')
        break
    elif choice == 2:
        print(f'The number {number} in octal is {oct(number)}.')
        break
    elif choice == 3:
        print(f'The number {number} in hexadecimal is {hex (number)}.')
        break
    else:
        print('INVÁLID OPTION! CHOICE A NUMBER 1 TO 3!')
        
    
