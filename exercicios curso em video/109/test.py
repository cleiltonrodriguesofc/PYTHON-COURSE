import moeda
p = float(input('Digite um preço: '))
formatado = input('Deseja ver formatação da moeda brasileira ou americana? ').lower()
if formatado in 'br':
    print(f'{moeda.moeda(p)} aumentado em 10% é {moeda.moeda(moeda.aumentar(p, 10))}')
    print(f'{moeda.moeda(p)} diminuido em 20% é {moeda.moeda(moeda.diminuir(p, 20))}')
    print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
    print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
else:
    print(f'{p} aumentado em 10% é {moeda.aumentar(p, 10)}')
    print(f'{p} diminuido em 20% é {moeda.diminuir(p, 20)}')
    print(f'O dobro de {p} é {moeda.dobro(p)}')
    print(f'A metade de {p} é {moeda.metade(p)}')