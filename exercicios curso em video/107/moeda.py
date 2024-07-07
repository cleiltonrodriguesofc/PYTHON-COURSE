'''Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade(). Faça também um programa que 
importe esse módulo e use algumas dessas funções.'''
def aumentar(preco, taxa):
    resposta = preco + (preco * taxa/100)
    return resposta


def diminur(preco, taxa):
    resposta = preco - (preco * taxa/100)
    return resposta


def dobro(preco):
    resposta = preco * 2
    return resposta


def metade(preco):
    resposta = preco / 2
    return resposta


