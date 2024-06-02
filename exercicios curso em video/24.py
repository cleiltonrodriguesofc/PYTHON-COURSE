city = input('Enter a city name: ').strip()
name = 'SANTO'
first_name = city.split()[0].upper()
if first_name == name:
    print('The city name start in "SANTO"')
else:
    print("""The city name don't start in "SANTO".""")
