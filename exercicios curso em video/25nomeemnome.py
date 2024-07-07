name = str(input('Enter your name: ')).strip()
has_or_no = name.upper().find('SILVA')
if has_or_no >= 0:
    print(f"The name SILVA it's in {name.title()}.")
else:
    print(f"The name SILVA it isn't in {name.title()}.")

#print(f'o nome {'SILVA' in name.upper()}') ***another way to do this exercise***
