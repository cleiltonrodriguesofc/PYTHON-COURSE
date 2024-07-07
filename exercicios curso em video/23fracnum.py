number = int(input('Enter a number of 0 at 9999: '))
thousands = number // 1000 % 10
hundreds = number // 100 % 10
tens = number // 10 % 10
ones = number // 1 % 10
print(f'Thousands: {thousands}\nHundreds: {hundreds}\nTens: {tens}\nOnes: {ones}')