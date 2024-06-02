'''Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores ‘M’ ou ‘F’. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''
sex = ''
print('ENTER "P" TO STOP.')
while True:
    sex = input('ENTER YOUR SEX: ').upper()
    if sex == 'M' or sex == 'F':
        continue
    elif sex == 'P':
        print('LEAVING PROGRAM.')
        break
    else: 
        print('INVALID OPTION! ENTER AGAIN.')