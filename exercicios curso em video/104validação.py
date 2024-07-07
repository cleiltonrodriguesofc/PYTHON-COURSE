'''Crie um programa que tenha a função leiaInt(), que vai funcionar de 
forma semelhante ‘a função input() do Python, só que fazendo a validação 
para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''
def leiaInt(mensagem):
    while True:
        try:
            valor_mensagem = int(input(mensagem))
            return valor_mensagem
        except ValueError:
            print('Erro! Digite um número inteiro válido.')

def leiaFloat(mensagem):
    while True:

        try:
            valor_float = float(input(mensagem))
            return valor_float
        except ValueError:
            print('Erro! Digite um número real.')


inteiro = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {inteiro}.')

flutuante = leiaFloat('Digite um número real: ')
print(f'Você digitou {flutuante}')