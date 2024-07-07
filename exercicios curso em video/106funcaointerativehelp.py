'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário 
vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a 
palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''
from time import sleep
c = ('\033[m',          #0-sem cor
       '\033[0;30;41m',   #1-vermelho
       '\033[0;30;42m',   #2-verde
       '\033[0;30;43m',   #3-amarelo
       '\033[0;30;44m',   #4-azul
       '\033[0;30;45m',   #5-roxo
       '\033[7;30m'      #6-branco
       )

def ajuda(comando):
    sleep(0.5)
    print(c[3])
    titulo(f'   Acessando manual')
    print(c[0])
    sleep(2)
    for _ in range(1, 4):
        print(' . ', end='', flush=True)
        sleep(0.8)
    print(c[2])
    help(comando)
    print(c[0])
    
 
def titulo(msg):
    tam = len(msg)//2
    
    print('=~='*tam)
    print(f'  {msg}  ')
    print('=~='*tam)
    
   
comando = ''
while True:
    print(c[4])
    titulo('HELP SYSTEM')
    print(c[0])
    comando = input('Função ou Biblioteca >> ').lower()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
sleep(1)
print(c[1])
titulo('GOOD BYE')
print(c[0])
