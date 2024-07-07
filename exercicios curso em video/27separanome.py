full_name = input('Enter your full name: ').strip()
first = full_name.split()[0]
last = full_name.split()[-1]
print(f'FIRST NAME: {first.title()}')
print(f'LAST NAME: {last.title()}')
