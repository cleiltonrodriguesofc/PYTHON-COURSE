"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%."""
salary = float(input('Enter your salary: '))
if salary > 1250:
    increase = salary * 1.1
    print(f'Your salary will be R$ {increase}.')
else:
    increase = salary * 1.15
    print(f'Your salary will be R$ {increase}.')