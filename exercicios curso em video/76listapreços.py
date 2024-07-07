'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos 
preços, na sequência. No final, mostre uma listagem de preços, organizando os dados.txt em forma
tabular.'''
products = ('Arroz', 31, 'Feijão', 9, 'Sabão', 7, 'Café', 7.5, 'Biscoito', 5.55)
print('='*43)
print(f'|{'TABLE PRODUCTS':^41}|')
print('='*43)
for position in range(0, len(products)):
    if position % 2 == 0:
        print(f'| {products[position]:.<30} R$ ', end='')
    else:
        print(f'{products[position]:>5.2f} |')
print('='*43)