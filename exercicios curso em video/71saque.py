'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, 
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai 
informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

quant_50 = 0
quant_20 = 0
quant_10 = 0
quant_1 = 0
while True:
    saque = int(input('Enter the request value: '))
    restante = saque
    while restante >= 50:
        restante -= 50
        quant_50 += 1
        restante = restante
    while restante >= 20:
        restante -= 20
        quant_20 += 1
        restante = restante
    while restante >= 10:
        restante -= 10
        quant_10 += 1
        restante = restante
    while restante >= 1:
        restante -= 1
        quant_1 += 1
        restante = restante
    break
print('NOTAS DO SAQUE')
if quant_50 > 0:
    print(f'Notas de 50: {quant_50}')
if quant_20 > 0:
    print(f'Notas de 20: {quant_20}')
if quant_10 > 0:
    print(f'Notas de 10: {quant_10}')
if quant_1 > 0:
    print(f'Notas de 1: {quant_1}')