'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora
 a possibilidade da digitação de um número de tipo inválido. Aproveite e 
 crie também uma função leiaFloat() com a mesma funcionalidade.'''
def leiaInt(mensagem):
    while True:
        try:
            inteiro = int(input(mensagem))
            return inteiro
        except ValueError:
            print('Valor inválido! Tente novamente.')

valor = leiaInt('Digite um número: ')
print(f'Você digitou o número {valor}')
