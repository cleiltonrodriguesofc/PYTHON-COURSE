'''Crie um programa que tenha uma função fatorial() que receba dois 
parâmetros: o primeiro que indique o número a calcular e outro chamado 
show, que será um valor lógico (opcional) indicando se será mostrado ou 
não na tela o processo de cálculo do fatorial.'''
def fatorial(numero, show=True):
    '''
    Calcula o fatorial de um número
    numero = numero a ser fatoriado
    show = opcional para mostrar o resultado
    return = retorna o resultado
    '''
    resultado = 1
    while numero > 0:
        resultado *= numero
        if show:
            print(f'{numero}', end='')
            if numero > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        numero -= 1
    return resultado

# FUNÇÃO PRINCIPAL
numero = int(input('Digite um número: '))
mostrar = input('Deseja mostrar a operação?[S/N] ').strip().upper()
print(f'O resultado do fatorial do número {numero} é:')
if mostrar == 'S':
    print(fatorial(numero, show=True))
else:
    print(fatorial(numero, show=False))
