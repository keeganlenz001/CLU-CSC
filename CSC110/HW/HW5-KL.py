# Name: Keegan Lenz
# Date: 9/30/2021
# Project Description: Helps user practice arithmetic
import random

num1 = 0
num2 = 0
answer = 0

difficulty = input('Would you like a Easy, Medium, or Hard problem?')

operator = input('What operator would you to practice with (+, -, *, /, %)')


def add():
    if difficulty == 1:
        global num1
        global num2
        global answer
        num1 = random.randrange(100, 200)
        num2 = random.randrange(100, 200)
        answer = num1 + num2
        print('What is', num1, '+', num2)



if operator == '+':
    add()

user_answer = input()
if user_answer == answer:
    print('Good job, you got it right!')
else:
    print('Sorry, that is the wrong answer')


