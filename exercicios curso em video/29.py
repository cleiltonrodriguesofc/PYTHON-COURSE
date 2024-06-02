""""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.

MAKE A PROGRAM THAT TO READ THE SPEED OF A CAR.
IF IT EXCEEDS 80KM/H, SHOW IT A MESSAGE SAYING THAT IT HAS BEEN FINED.
THE FIN WILL BE R$ 7,00 BY EACH KM ABOVE THE LIMIT. 
"""
speed = float(input('Enter the speed: '))
fin = 7
if speed > 80:
    print(f'YOU WERE FINED IN R$ {(speed - 80) * 7}.')
else:
    print('YOU WERE NOT FINED.')