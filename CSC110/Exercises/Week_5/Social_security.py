import random

# input('What is your name: ')
# input('What is you last name: ')
# input('What is you date of birth: ')
# print()
print('Your social security number is:', end=" ")

for i in range(3):
    num = str(random.randrange(0, 9))
    print(num, end="")

print('-', end="")

for i in range(2):
    num = str(random.randrange(0, 9))
    print(num, end="")

print('-', end="")

for i in range(4):
    num = str(random.randrange(0, 9))
    print(num, end="")

