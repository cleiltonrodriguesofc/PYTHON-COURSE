'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, 
O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''
phrase = input('ENTER A PHRASE: ').strip().upper()
words = phrase.split()
together = ''.join(words)
reverse = together[::-1]
if reverse == together:
    print(f'THE PHRASE "{phrase}" IS A PALINDROME')
else:
    print(f'THE PHRASE "{phrase}" IS NOT A PALINDROME')