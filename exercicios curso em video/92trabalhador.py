'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho
 e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for 
 diferente de ZERO, o dicionário receberá também o ano de contratação e o 
 salário. Calcule e acrescente, além da idade, com quantos anos a pessoa 
 vai se aposentar.'''
# digamos que a pessoa se aposente com 30 anos de contrato ou 60 anos de idade
trabalhadores = []
trabalhador = {}
while True:
    trabalhador['NOME'] = input('Digite o nome: ').strip().upper()
    while True:
        trabalhador['SEXO'] = input('Digite o sexo[M/F] ').strip().upper()
        if trabalhador['SEXO'] in 'MF':
            break
    trabalhador['IDADE'] = (2024 - int(input('Digite o ano de nascimento: ')))
    trabalhador['CTPS'] = int(input('Digite o número da CTPS: '))
    if trabalhador['CTPS'] != 0:
        trabalhador['ANO DE CONTRATAÇÃO'] = int(input('Digite o ano do contrato: '))
        trabalhador['SALÁRIO'] = float(input('Digite o salário: '))
    trabalhadores.append(trabalhador.copy())
    while True:
        continuar = input('Cadastrar mais?[S/N] ').strip().upper()
        if continuar == 'S':
            break
        if continuar == 'N':
            break
        else:
            print('Opção inválida!')
    if continuar == 'N':
        break
print(trabalhador)
for dado in trabalhadores:
    print('=-='*10)
    print(f'======== {dado['NOME']} ========')
    print(f'SEXO: {dado['SEXO']}')
    print(f'IDADE: {dado['IDADE']}\nPOR IDADE SE APOSENTA EM {60-dado['IDADE']} ANOS - EM {(60-dado['IDADE'])+2024}')
    print(f'CTPS: {dado['CTPS']}')
    print(f'ANO DE CONTRATAÇÃO: {dado['ANO DE CONTRATAÇÃO']}\nPOR TEMPO DE SERVIÇO SE APOSENTA EM {dado['ANO DE CONTRATAÇÃO']+30} - COM {(dado['ANO DE CONTRATAÇÃO']-(2024-dado['IDADE']))+30} ANOS DE IDADE')
    print(f'SALÁRIO: {dado['SALÁRIO']}')

