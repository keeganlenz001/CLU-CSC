class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def grade_percent(self):
        if self.grade >= 90:
            new_grade = 'A'
        elif self.grade >= 80:
            new_grade = 'B'
        elif self.grade >= 70:
            new_grade = 'C'
        elif self.grade >= 60:
            new_grade = 'D'
        else:
            new_grade = 'F'
        return new_grade


class Person(Student):
    def __init__(self, last_name):
        self.last_name = last_name


s1 = Student('John', '2021-2', 85.6)
p1 = Person('Lennon')
print('Student Name:', s1.name, p1.last_name)
print('Student ID:', s1.student_id)
print('Grade:', s1.grade_percent())

