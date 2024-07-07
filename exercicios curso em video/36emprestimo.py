"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""
home_value = float(input('Enter the home value: '))
salary = float(input('Enter your salary: '))
spend_time = int(input('Enter how long in years you intend to pay that for: '))
# home value about spend time
pmt = home_value / (spend_time*12)
print(f'The monthly installment value is R$ {pmt:.2f}.')
print(f'You can pay monthly {salary*0.3:.2f}')
if pmt > (salary*0.3):
    print("You can't do this operation, loan denied!")
else:
    print("All right! You can do this operation, authorized loan!.")