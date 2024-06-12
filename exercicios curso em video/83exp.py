'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos 
e fechados na ordem correta.'''
exp = str(input('Enter a expression: '))
parentese_aberto = []
parentese_fechado = []
for simb in exp:
    if simb == '(':
        parentese_aberto.append('(')
    elif simb == ')':
        parentese_fechado.append(')')

if len(parentese_aberto) == len(parentese_fechado):    
    print('Your expression is correct.')
else:
    print('Your expression is not correct.')