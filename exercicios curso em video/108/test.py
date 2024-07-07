import moeda
p = float(input('Digite um preço: '))
print(f'{moeda.moeda(p)} aumentado em 10% é {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'{moeda.moeda(p)} diminuido em 20% é {moeda.moeda(moeda.diminur(p, 20))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')