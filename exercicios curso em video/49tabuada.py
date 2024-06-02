'''Refaça o DESAFIO 9, mostrando a tabuada de um número que o 
usuário escolher, só que agora utilizando um laço for.'''
# DEFINIR NÚMERO
# DEFINIR TABUADA
# SOLICITAR ENTRADA DE NÚMERO
num = int(input('DIGITE O NÚMERO QUE VOCÊ QUER A TABUADA: '))
print('ESCOLHA UMA TABUADA:')
print('''1. ADIÇÃO
2. SUBTRAÇÃO
3. MULTIPLICAÇÃO
4. DIVISÃO''')
while True:
    escolha = int(input('QUAL TABUADA VOCÊ QUER? '))
    if escolha == 1:
        print('TABUADA DE ADIÇÃO ESCOLHIDA')
        for i in range(1, 10):
            print(f'{num} + {i} = {num + i}')
        break
    elif escolha == 2:
        print('TABUADA DE SUBTRAÇÃO ESCOLHIDA')
        for i in range(1, 10):
            print(f'{num} - {i} = {num - i}')
        break
    elif escolha == 3:
        print('TABUADA DE MULTIPLICAÇÃO ESCOLHIDA')
        for i in range(1, 10):
            print(f'{num} * {i} = {num * i}')
        break
    elif escolha == 4:
        print('TABUADA DE DIVISÃO ESCOLHIDA')
        for i in range(1, 10):
            print(f'{num} / {i} = {num / i:.2f}')
        break
    else:
        print('OPÇÃO INVÁLIDA!')
    