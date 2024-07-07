from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'dados.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    cabec('MENU DO SISTEMA')
    menu(['Ver cadastro', 'Cadastrar', 'Sair do programa'])
    resp = leiaInt('Digite uma opção: ')
    if resp == 1:
        lerArquivo(arq)
        sleep(2)
    elif resp == 2:
        cabec('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt(('Idade: '))
        cadastrar(arq, nome, idade)
        sleep(2)
    elif resp == 3:
        print('Saindo do programa...')
        sleep(1)
        break
    else:
        print('Erro! Opção inválida')