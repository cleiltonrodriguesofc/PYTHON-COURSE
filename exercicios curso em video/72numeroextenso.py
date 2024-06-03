'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por 
extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 
e 20) e mostrá-lo por extenso.'''

numbers = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
number = int(input('Enter a number 0 to 20: '))
print(f'You entered the number {numbers[number].upper()}.')