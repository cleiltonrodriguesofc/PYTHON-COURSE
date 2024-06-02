''''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns 
termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

p1 = int(input('ENTER THE FIRST TERM: '))
r = int(input('ENTER THE PROGRESSION REASON: '))
term = p1
counter = 1
more = 10
total = 0
while more != 0:
    total += more
    while counter <= total:
        print(f'{term} -> ', end='')
        term += r
        counter += 1
    print('PAUSA')
    more = int(input('HOW MANY TERMS DO YOU WANT TO SHOW MORE: '))
print(f'ARITHMETIC PROGRESSION FINALIZED WITH {total} TERMS.')
print('FIM')