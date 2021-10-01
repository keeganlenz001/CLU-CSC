num_of_students = int(input('How many students are in the class: '))
highest_grade = 0
best_student = ''

for i in range(num_of_students):
    name = input('Name of student: ')
    grade = float(input('Grade they got out of 100: '))
    if highest_grade < grade:
        highest_grade = grade
        best_student = name
    print()

print('The student with the highest score is:', best_student)


