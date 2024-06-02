'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''
words = ("Algorithm", "Variable", "Loop", "Function", "Class", "Method", "Compiler", "Debugging", "Library", "Inheritance")
for word in words:
    print(f'\nThe word {word.upper()} has the vowels: ', end='')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f'{letter.lower()}', end=' ')