''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa 
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, 
mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''
maior18 = 0
homens = 0
mulhermenor20 = 0
continuar = ' '
while continuar != 'N':
    print('='*20)
    print('CADASTRE UMA PESSOA')
    print('='*20)
    try:
        idade = int(input('Digite sua idade: '))
        if idade > 18:
            maior18 += 1
       
    except ValueError():
        print('Opção inválida!')
        continue
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite seu sexo: ').upper().strip()[0]
        print('='*20)
        if sexo == 'M':
            homens += 1
        if idade < 20 and sexo == 'F':
            mulhermenor20 +=1
            continue
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar?[S/N]').upper().strip()[0]
        if continuar == 'S':
            continue
        if continuar == 'N':
            print('='*20)
            print(f'São {maior18} pessoas maiores que 18 anos')
            print(f'Foram {homens} homens cadastrados.')
            print(f'Foram cadastradas {mulhermenor20} mulheres menores que 20 anos.')
            print('='*20)
            print('Saindo do programa...')
            break
        else: 
            print('Opção inválida!')
                       
    

