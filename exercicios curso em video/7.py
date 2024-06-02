import statistics
grades = []
for i in range(1, 3):
    grade = float(input('Enter your note: '))
    grades.append(grade)
m = statistics.mean(grades)
print(f'The mean of grades is {m}.')
