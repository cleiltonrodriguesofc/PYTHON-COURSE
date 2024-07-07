'''Crie um programa que tenha uma função chamada voto() que vai receber 
como parâmetro o ano de nascimento de uma pessoa, retornando um valor 
literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO 
nas eleições.'''
from datetime import date as dt
import time
def voto(nascimento):
    atual = dt.today().year
    idade = atual - nascimento
    if idade < 16:
        return 'VOTO NEGADO'
    if 60 >= idade >= 16:
        return 'OBRIGATÓRIO'
    else:
        return 'OPCIONAL' 
    
# programa principal 
nascimento = int(input('Ano de nascimento: '))
print(f'Avaliando seu ano de nascimento...')
time.sleep(2)
print('PESSOAS MENORES DE 16 ANOS NÃO PODEM VOTAR...')
time.sleep(1)
print('PESSOAS MAIORES QUE 60 ANOS, VOTO É OPCIONAL...')
time.sleep(1)
print('PESSOAS ENTRE 16 E 60 ANOS, VOTO OBRIGATÓRIO...')
time.sleep(1)
print('Com base nisso...')
print(f'Seu voto é {voto(nascimento)}, você tem {2024-nascimento} anos de idade.')