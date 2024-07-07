def linha(tam=42):
    return '-'*tam

def cabec(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cont = 1
    for i in lista:
        print(f'{cont} - {i}')
        cont += 1
    print(linha())

def leiaInt(mensagem):
    while True:
        try:
            inteiro = int(input(mensagem))
            return inteiro
        except ValueError:
            print('Valor inválido! Tente novamente.')
