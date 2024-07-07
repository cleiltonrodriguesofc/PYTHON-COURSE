"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""
import statistics
numbers = []
for i in range(1, 4):
    num = float(input('Enter a number: '))
    numbers.append(num)
print(f'The largest number is {max(numbers)}')
print(f'The smallest number is {min(numbers)}')