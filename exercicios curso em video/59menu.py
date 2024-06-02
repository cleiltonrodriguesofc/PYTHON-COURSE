'''Crie um programa que leia dois valores e mostre um menu na tela: B

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
import time
print('-='*30)
n1 = int(input(f'ENTER THE FIRST VALUE: '))
n2 = int(input(f'ENTER THE SECOND VALUE: '))
values = [n1, n2]
while True:
    print('''SELECT A OPTION
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
''')
    print('-='*30)
    option = int(input('CHOICE A OPTION: '))
    if option == 1:
        soma = n1 + n2
        print(f'THE SUM OF THE 2 NUMBERS IS {soma}')
    if option == 2:
        product = n1 * n2
        print(f'THE PRODUCT OF THE 2 NUMBERS IS {product}')
    elif option == 3:
        maior = max(values)
        print(f'THE BIGGEST NUMBER OF THE 2 NUMBERS IS {maior}')
    elif option == 4:
        print('ENTER THE VALUES AGAIN!')
        n1 = int(input(f'ENTER THE FIRST VALUE: '))
        n2 = int(input(f'ENTER THE SECOND VALUE: '))
    elif option == 5:
        print('YOU CHOICED TO LEAVE PROGRAM.')
        time.sleep(2)
        print('LEAVING PROGRAM...')
        break
    else: 
        print('INVALID OPTION! TRY AGAIN.')
    