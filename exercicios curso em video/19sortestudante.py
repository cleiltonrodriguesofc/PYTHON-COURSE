import random
students = []
for i in range(1, 5):
    student = input('Enter the student name: ')
    students.append(student)
lucked = random.choice(students)
print(f'The student drawn to clear the board is {lucked}')
