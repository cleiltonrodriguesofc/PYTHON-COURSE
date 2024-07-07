'''Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''
product = float(input('Enter the price product: '))
print('''
    CHOICE A PAYMENT OPTION:
      1. IN CASH OR CHECK: 10% OFF
      2. CASH ON CARD: 5% OFF
      3. 2X: NORMAL PRICE
      4. 3X OR MORE ON CARD: 20% INTEREST''')
while True:
    choice = int(input('CHOICE A NUMBER: '))
    if choice == 1:
        print(f'The price product will be R$ {product*0.9:.2f}')
        break
    elif choice == 2:
        print(f'The price product will be R$ {product*0.95:.2f}')
        break
    elif choice == 3:
        x = int(input('How many time do you pay that: '))
        print(f'The price product will be R$ {product:.2f}, NORMAL PRICE')
        break
    elif choice == 4:
        print(f'The price product will be R$ {product*1.2:.2f}')
        break
    else:
        print('INVALID CHOICE! PLEASE, CHOICE A NUMBER FROM 1 TO 4!')