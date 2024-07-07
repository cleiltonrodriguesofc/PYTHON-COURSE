km = float(input('Enter the amount of mileage driven: '))
total_value = km * 0.15
rent = int(input('Enter the amount of rented days: '))
rent_day = rent * 60
print(f'The value of the rent is {rent_day} and the value of the km is {total_value}, so the price to pay is {rent_day+total_value}.')