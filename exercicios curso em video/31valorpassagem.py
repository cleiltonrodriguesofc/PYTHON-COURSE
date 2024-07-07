"""Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens 
de até 200Km e R$0,45 parta viagens mais longas."""

km = float(input('Enter how much km is your travel: '))
if km <= 200:
    ticket = km * 0.5
    print(f'Your ticket is R$ {ticket}.')
else:
    ticket = km * 0.45
    print(f'Your ticket is R$ {ticket}')