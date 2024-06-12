'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores 
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''

valores = [[], [], []]
print('Digite 3 valores.')
for i in range(1,4):
    valores[0].append(int(input('Digite um valor: ')))
print('Digite mais 3 valores.')
for i in range(1,4):
    valores[1].append(int(input('Digite um valor: ')))
print('Digite mais 3 valores.')
for i in range(1,4):
    valores[2].append(int(input('Digite um valor: ')))
print('A matriz é:')
print(valores[0])
print(valores[1])
print(valores[2])