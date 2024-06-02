'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

height = float(input('Enter your height: '))
weight = float(input('Enter your weight: '))
bmi = weight / (height**2)
if bmi < 18.5:
    print(f'Your BMI is {bmi:.2f}. YOU ARE UNDERWEIGHT.')
elif bmi >= 18.5 and bmi < 25:
    print(f'Your BMI is {bmi:.2f}. You are at the IDEAL WEIGHT.')
elif bmi >= 25 and bmi < 30:
    print(f'Your BMI is {bmi:.2f}. You are OVERWEIGHT.')
elif bmi >= 30  and bmi < 40:
    print(f'Your BMI is {bmi:.2f}. You are OBESE.')
elif bmi >= 40:
    print(f'Your BMI is {bmi:.2f}. You are at the MORBID OBESITY.')