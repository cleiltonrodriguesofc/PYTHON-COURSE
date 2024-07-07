import moeda
p = float(input('Digite um preço: '))
print(f'O preço {p} aumentado em 10% é {moeda.aumentar(p, 10)}')
print(f'O preço {p} diminuido em 20% é {moeda.diminur(p, 20)}')
print(f'O dobro do preço {p} é {moeda.dobro(p)}')
print(f'A metade do preço {p} é {moeda.metade(p)}')