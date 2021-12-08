class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_name(self):
        print('Hello, my name is ' + self.name)

    def display_age(self):
        print('I am', str(self.age), 'years old')

    def set_address(self, address):
        self.address = address

    def display_address(self):
        print('I am from ' + self.address)


p1 = Person('John', 36, 'Liverpool')

p1.display_name()
p1.display_age()
p1.display_address()
p1.display_name()
p1.set_address('CLU')

print('Hey, I moved to', p1.address + '!')
