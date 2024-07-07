import random
students = []
for i in range(1, 5):
    student = input('Enter the student name: ')
    students.append(student)
random.shuffle(students)

print("Random order of student names:")
for position, name in enumerate(students, start=1):
    print(f"{position}. {name}")
