class Person:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email


class Student(Person):
    def __init__(self, name, address, phone_number, email, class_status):
        super().__init__(name, address, phone_number, email)
        self.class_status = class_status


class Employee(Person):
    def __init__(self, name, address, phone_number, email, office_number, salary, date_hired):
        super().__init__(name, address, phone_number, email)
        self.office_number = office_number
        self.salary = salary
        self.data_hired = date_hired


class Staff(Employee):
    def __init__(self, office_number, salary, date_hired, rank):
        super().__init__(office_number, salary, date_hired)
        self.rank = rank


class Faculty(Employee):
    def __init__(self, office_number, salary, date_hired, office_hours, rank):
        super().__init__(office_number, salary, date_hired)
        self.office_hours = office_hours
        self.rank = rank


p1 = Person('John Lennon', 'CLU', '(559)-123-4567', 'jlennon@callutheran.edu')
print(p1.name)

s1 = Student(p1.name, p1.address, p1.phone_number, p1.email, 'Freshman')
print('Welcome', s1.name, 'to CLU as a', s1.class_status)

# e1 = Employee(p1.name, p1.address, p1.phone_number, p1.email, '110', '$25,000', '11/16/2020')


