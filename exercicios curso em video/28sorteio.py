import random
import time
#computar números aleatórios de 0 a 5
pc = random.randint(0, 5)
#solicitar entrada de número pelo usuário
print("I'M GOING TO THINK IN A NUMBER OF 0 AT 5, TRY TO GUESS!")
time.sleep(2)
num = int(input('WHAT IS THE NUMBER? '))
print('PROCECSING...')
time.sleep(3)
if num == pc:
    print(f'CONGRATULATIONS! I thinked in {pc}, your choice is {num} and you WON!')
else:
    print(f'SORRY! I thinked in {pc}, your choice is {num} and you LOST.')