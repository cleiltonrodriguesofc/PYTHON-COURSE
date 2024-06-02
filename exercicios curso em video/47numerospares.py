'''Crie um programa que mostre na tela todos 
os números pares que estão no intervalo entre 1 e 50.'''
listapares = []
for i in range(1, 51):
    if i % 2 == 0:
        listapares.append(i)
print(f'OS NÚMEROS PARES ENTRE 1 E 50 SÃO:')
print(*listapares)