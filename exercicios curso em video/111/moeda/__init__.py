def aumentar(preco=0, taxa=0):
    resposta = preco + (preco * taxa/100)
    return resposta


def diminuir(preco=0, taxa=0):
    resposta = preco - (preco * taxa/100)
    return resposta


def dobro(preco=0):
    resposta = preco * 2
    return resposta


def metade(preco=0):
    resposta = preco / 2
    return resposta

def moeda(preco=0, moeda='R$'):
    return f'{moeda} {preco:.2f}'.replace('.', ',')

def resumo(p=0, txmais=0, txmenos=0): 
    formatado = input('Quer formatação da moeda brasileira ou americana? ').lower()
    print('=~='*10)
    print('RESUMO'.center(30))
    print('=~='*10)
    print()
    print(f'Analisando o preço {moeda(p)}')
    print()
    if formatado in 'br':
        print(f'{moeda(p)} aumentado em {txmais}% é {moeda(aumentar(p, txmais))}')
        print(f'{moeda(p)} diminuido em {txmenos}% é {moeda(diminuir(p, txmenos))}')
        print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
        print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
        return formatado
    else:
        print(f'{p} aumentado em {txmais}% é {aumentar(p, txmais)}')
        print(f'{p} diminuido em {txmenos}% é {diminuir(p, txmenos)}')
        print(f'O dobro de {p} é {dobro(p)}')
        print(f'A metade de {p} é {metade(p)}')
        
        

