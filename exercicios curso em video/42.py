'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''
line1 = float(input('Enter first segment: '))
line2 = float(input('Enter second segment: '))
line3 = float(input('Enter third segment: '))
if line1 < line2 + line3 and line2 < line1 + line3 and line3 < line2 + line1:
    print('It forms a triangle')
    if line1 == line2 == line3:
        print('It is a EQUILATERAL TRIANGLE')
    elif line1 == line2 or line2 == line3 or line1 == line3:
        print('It is a ISOSCELES TRIANGLE')
    else:
        print('It is a SCALENE TRIANGLE')
else:
    print("It doesn't form a triangle.")