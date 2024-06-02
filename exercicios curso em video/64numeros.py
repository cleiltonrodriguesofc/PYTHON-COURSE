'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai 
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando 
o flag).'''
print('-*'*10)
print('ENTER "999" TO STOP.')
print('-*'*10)
numbers = []
while True:
    try:
        number = int(input('ENTER A NUMBER: '))
        if number != 999:
            numbers.append(number)
        if number == 999:
            print('YOU INSERTED "999". LEAVING PROGRAM...')
            print('-*'*10)
            break
    except ValueError:
        print('INVALID OPTION! TRY AGAIN.')
        pass
print('-*'*10)
print(f'THE INSERTED NUMBERS ARE: ', end='')
print(*numbers)
print('-*'*10)
print(f'YOU INSERTED {len(numbers)} NUMBERS')
print('-*'*10)
print(f'THEIR SUM IS {sum(numbers)}')
print('-*'*10)