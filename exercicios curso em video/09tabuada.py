#definir range de números da tabuada de adição, subtração, multiplicação e divisão
#depois calcular e imprimir tabela
num = int(input('Insira um número: '))
print(f'A tabuada de adição do número {num} é:\n')
for i in range(0, 10):
  soma = i + num
  print(f'{i} + {num} = {soma}')
print(f'\nA tabuada de subtração do número {num} é:\n')
for i in range(0, 10):
  subtracao = num - i
  print(f'{num} - {i} = {subtracao}')
print(f'\nA tabuada de multiplicação do número {num} é:\n')
for i in range(0, 10):
  multiplicacao = i * num
  print(f'{num} * {i} = {multiplicacao}')
print(f'\nA tabuada de divisão do número {num} é:\n')
for i in range(1, 10):
  divisao = num / i
  print(f'{num} / {i} = {divisao:.2f}')

