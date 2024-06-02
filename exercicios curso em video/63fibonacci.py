''' Escreva um programa que leia um número N inteiro qualquer e mostre na tela os 
N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''


print('-*-'*10)
print('--**-FIBONACCI SEQUENCE-**--')
print('-*-'*10)
t1 = 0
t2 = 1
terms = int(input('HOW MANY TERMS DO YOU WANT TO SHOW? '))
print(f'{t1} -> {t2} -> ', end='')
counter = 3
while counter <= terms:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    counter += 1
    t1 = t2
    t2 = t3
print('END')