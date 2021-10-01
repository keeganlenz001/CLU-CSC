import random

num2 = random.randint(0, 10)
num1 = num2 + random.randint(0, 10)

print('What is', num1, '-', num2)
answer = int(input())

if answer == (num1 - num2):
    print('Your are correct!')
else:
    print('Something went wrong')

