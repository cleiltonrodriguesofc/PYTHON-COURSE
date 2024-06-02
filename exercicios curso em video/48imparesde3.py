'''Faça um programa que calcule a soma entre todos os números que são 
múltiplos de três e que se encontram no intervalo de 1 até 500.'''
listaimpares = []
for n in range(1, 501, 2):
    if n % 3 == 0:
        listaimpares.append(n)
# SOMAR NÚMEROS IMPARES MULTIPLOS DE 3
soma  = sum(listaimpares)
print(f'A SOMA DOS NÚMEROS ÍMPARES MULTIPLOS DE 3 DE 1 A 500 É: {soma}')