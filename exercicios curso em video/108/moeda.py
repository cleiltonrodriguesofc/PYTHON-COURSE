'''Adapte o código do desafio #107, criando uma função adicional 
chamada moeda() que consiga mostrar os números como um valor monetário 
formatado.'''
def aumentar(preco=0, taxa=0):
    resposta = preco + (preco * taxa/100)
    return resposta


def diminur(preco=0, taxa=0):
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

