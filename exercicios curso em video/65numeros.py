'''Crie um programa que leia vários números inteiros pelo teclado. No final da 
execução, mostre a média entre todos os valores e qual foi o maior e o menor valores 
lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar 
valores.'''
import statistics
answer = 'S'
numbers = []
while answer in 'Ss':
    num = int(input('ENTER A NUMBER: '))
    numbers.append(num)
    answer = input('DO YOU WANNA CONTINUE?[S/N] ').upper().strip()
print('END')
print(f'THE MEAN OF NUMBERS IS {statistics.mean(numbers)}.')
print(f'THE BIGGEST VALUE IS {max(numbers)}.')
print(f'THE SMALLER VALUE IS {min(numbers)}.')