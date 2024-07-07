'''Faça um programa que tenha uma função chamada maior(), que receba vários
 parâmetros com valores inteiros. Seu programa tem que analisar todos os 
 valores e dizer qual deles é o maior.'''
def maior(valores):
    maior_valor = max(valores)
    print(f'O maior valor inserido foi {maior_valor}')
    

# PROGRAMA PRINCIPAL
valores = []
while True:
    valor = int(input('Digite um número: '))
    valores.append(valor)
    while True:
        continuar = input('Continuar?[S/N] ').strip().upper()
        if continuar in 'SN':
            break
        else:
            print('Opção inválida!')
    if continuar == 'N':
        break
maior(valores)