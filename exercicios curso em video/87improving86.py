'''Aprimore o desafio anterior, mostrando no final: 

A) A soma de todos os valores pares digitados.

B) A soma dos valores da terceira coluna.

C) O maior valor da segunda linha.'''

valores = [[], [], []]
pares = []
print('Digite 3 valores.')
for i in range(1,4):
    valor = int(input('Digite um valor: '))
    valores[0].append(valor)
    # colocar em pares
    if valor % 2 == 0:
        pares.append(valor)
print('Digite mais 3 valores.')
for i in range(1,4):
    valor1 = int(input('Digite um valor: '))
    valores[1].append(valor1)
    # colocar em pares
    if valor1 % 2 == 0:
        pares.append(valor1)
print('Digite mais 3 valores.')
for i in range(1,4):
     valor2 = int(input('Digite um valor: '))
     valores[2].append(valor2)
     if valor2 % 2 == 0:
        pares.append(valor2)
print('A matriz é:')
print(valores[0])
print(valores[1])
print(valores[2])
# somar pares
print(f'A soma dos pares digitados é {sum(pares)}')
soma = valores[0][2] + valores[1][2] + valores[2][2]
print(f'A soma dos valores da terceira coluna é {soma}')
maiorlinha2 = max(valores[1])
print(f'O maior valor da segunda linha é {maiorlinha2}')
