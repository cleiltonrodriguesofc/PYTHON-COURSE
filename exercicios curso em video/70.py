'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá 
perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
# product name
# product price
products = []
productmost1000 = []
prices = []
smallerproduct = ' '
# smallerprice = 0
while True:
    product = str(input('Enter a product name: '))
    products.append(product)
    price = float(input('Enter the product price: '))
    prices.append(price)
    if price == min(prices):
        smallerproduct = product
    else:
        pass
    if price > 1000:
        productmost1000.append(price)
    continuar = ' '
    while continuar not in 'YN':
        continuar = input('Do you want to continue?[Y/N] ').upper().strip()[0]
        if continuar == 'Y':
            continue
        if continuar == 'N':
            print('Leaving program...')
            break
    if continuar == 'N':
        break
# to sum
s = sum(prices)
print(f'The purchase cost R$ {s}')
# how many product are most 1000
most1000 = len(productmost1000)
print(f'Are {most1000} most 1000 reais.')
# cheapest product
for price in prices:
    if price == min(prices):
        print(f'The cheapest product is {smallerproduct} and it is R$ {price}.')
