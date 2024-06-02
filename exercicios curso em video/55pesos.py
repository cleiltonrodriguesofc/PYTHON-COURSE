'''Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.'''
list_pesos = []
for p in range(1, 6):
    peso = float(input('ENTER YOUR WEIGHT: '))
    print('-'*20)
    list_pesos.append(peso)
bigger_weight = max(list_pesos)
smaller_weight = min(list_pesos)
print(f'THE BIGGER WEIGHT IS {bigger_weight}')
print(f'THE LOWER WEIGHT IS {smaller_weight}')