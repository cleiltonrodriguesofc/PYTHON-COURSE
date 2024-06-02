'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o número solicitado 
for negativo.'''
print('='*20)
print('='*5,'TABUADA', '='*5)
while True:
    print('='*20)
    number = int(input('Qual tabuada você quer?[Valor negativo para parar]: '))
    print('='*20)
    if number >= 0:
        for i in range(1, 11):
            print(f'{i} x {number} = {i*number}')
    if number < 0:
        print('Encerrando tabuada....')
        break