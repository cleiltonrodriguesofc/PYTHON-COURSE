width = float(input('Enter the width of the wall: '))
height = float(input('Enter the height of the wall: '))
area = width * height
ink = area / 2 #how much ink is it necessary to paint the wall?
#print wall area
print(
    f'The wall area is {area}m²\n'
    f"It's takes {ink} liters of paint to paint the wall."
)
